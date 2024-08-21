import sys, random, os

from gennpc import Npc, statlist
from load_initial import nationlist, factionlist, Faction
from location import Location
from genmeow import Cat

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#Generate initial location to save any potential NPCs
#defaultplace = Location("Unassigned", "Default")

npclist = []


#Break out posts so a banner appears if invalid combination attempted to be saved. Or warning that invalid combinations will be automatically resolved
@app.route("/", methods=["GET", "POST"])
def index():
    sexes = ["M", "F"]
    types = ["HUMAN", "SYNTH"]
    factionnames = []
    for faction in factionlist:
        factionnames.append(faction.name)
    if request.method == "GET":
        npc = Npc()
    if request.method =="POST":
        sex = request.form.get("sex")
        postfaction = request.form.get("faction")
        pstat = request.form.get("pstat")
        type = request.form.get("type")
        nation = request.form.get("namelist")
        postfaction = Faction.nametoid(postfaction)
        '''if postfaction not in factionnames:
            postfaction = ""'''
        '''if pstat not in statlist:
            pstat = ""
        else:'''
        for x in range(len(statlist)):
            if pstat == statlist[x]:
                pstat = x
                break
        '''if type not in types:
            type = ""
        if nation not in nationlist:
            nation = ""'''
        npc = Npc(sex=sex, factionid=postfaction, pstat=pstat, type=type, nation=nation)
    npcfactionname = Faction.idtoname(npc.factionid)
    pstat = statlist[npc.pstat]
    return render_template("index.html", namelist=nationlist, sexes=sexes, factions=factionnames, types=types, statlist=statlist, npc=npc, npcfaction=npcfactionname, pstat=pstat)
            

@app.route("/validatenpc", methods=["POST"])
def validatenpc():
        sex = request.form.get("gensex")
        pstat = request.form.get("genpstat")
        for x in range(len(statlist)):
            if pstat == statlist[x]:
                pstat = x
                break
        type = request.form.get("gentype")
        #nation = request.form.get("namelist")
        postfaction = request.form.get("genfaction")
        postfaction = Faction.nametoid(postfaction)
        forename = request.form.get("genforename")
        surname = request.form.get("gensurname")
        job = request.form.get("genjob")
        type = request.form.get("gentype")
        stats = [request.form.get("genstr"), request.form.get("genagl"), request.form.get("genwit"), request.form.get("genemp"), request.form.get("genhp")]
        npclist.append(Npc(sex=sex, factionid=postfaction, pstat=pstat, type=type, forename=forename, surname=surname, job=job, stats=stats))
        return redirect("/npcs")

@app.route("/npcs", methods=["GET", "POST"])
def npcs():
    if request.method == "GET" or "POST":
        npcstrings = []
        for x in range(len(npclist)):
            npcstrings.append(npclist[x])
    return render_template("npcs.html", npcstrings=npcstrings)

@app.route("/cats")
def cats():
    cat = Cat()
    print(cat)
    return render_template("cats.html", cat=cat)
        


