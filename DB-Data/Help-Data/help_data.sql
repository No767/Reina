--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Debian 14.5-1.pgdg110+1)
-- Dumped by pg_dump version 14.5 (Debian 14.5-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: help_data; Type: TABLE; Schema: public; Owner: Reina
--

CREATE TABLE public.help_data (
    uuid character varying NOT NULL,
    name character varying,
    parent_name character varying,
    description text,
    module character varying
);


ALTER TABLE public.help_data OWNER TO "Reina";

--
-- Data for Name: help_data; Type: TABLE DATA; Schema: public; Owner: Reina
--

COPY public.help_data (uuid, name, parent_name, description, module) FROM stdin;
c71dcb62-ae78-44e6-b166-9f0b0867cb0c	anilist search anime	anilist search	Searches for up to 25 animes on AniList	anilist
7fd84f19-202d-43da-b907-86ae538444fe	anilist search manga	anilist search	Searches for up to 25 mangas on AniList	anilist
bf70923a-ef37-480c-9c0b-f3c5afb311eb	anilist search tags	anilist search	Searches up to 25 animes and mangas based on the given tag	anilist
43977ede-e08f-4c72-91ae-e890b0b2feb8	anilist search users	anilist search	Provides up to 25 users from the given username	anilist
95280be1-26bd-4b51-b87d-1d601df02047	anilist search characters	anilist search	Searches up to 25 anime characters on AniList	anilist
84284786-2ed6-4e89-a025-feaf253d624b	anilist search actors	anilist search	Searches for up to 25 voice actors or staff that have worked on an anime and/or its characters	anilist
3cc387a0-0fe1-4f82-a58b-375df8e5dded	anilist search	anilist	Search for anime on AniList	discord.commands.core
121e2c5d-148e-4d6d-9ab5-fb4c1784034b	anilist	None	Commands for AniList service	discord.commands.core
2e3444cc-4d97-4bd5-8c74-b3a0505d6919	disquest rank local	disquest rank	Displays the most active members of your server!	disquest
19c2a86a-17ac-40f3-8b11-f8a8fc2632cc	disquest rank global	disquest rank	Displays the most active members of all servers that this bot is connected to!	disquest
afa3c069-b64b-489c-a0ab-d98cb76ae79b	disquest rank	disquest	Commands for Disquest	discord.commands.core
9b7b7a52-8f70-4fb8-b08f-b7dc4a07ccfc	disquest mylvl	disquest	Displays your activity level!	disquest
6dfaef26-b8cd-4830-9efe-ddd166afc5ea	disquest init	disquest	Initializes the database for DisQuest!	disquest
edde9146-757c-4a1d-ba68-d5c0c5b207fc	disquest	None	Commands for Disquest	discord.commands.core
09b9f8eb-4ab8-4555-a4d7-b0f39b4cbdcf	events view all	events view	Views all of your past and upcoming events	events
9f8696d1-05bb-4818-a01d-f6fbbdfe29e0	events view upcoming	events view	View all of your upcoming events	events
2c690860-7cf3-48cd-bca4-30b78d8e2d5e	events view past	events view	View all of your past events	events
2b751b95-81a7-413b-b0cc-0b0b7f44da59	events view countdown	events view	Checks how much days until an event will happen and pass	events
9119234a-5d6c-4164-a641-e1c4c3789431	events view	events	View the events	discord.commands.core
07c11850-de7c-4908-a297-0608464630fa	events delete one	events delete	Deletes one event from your list of events	events
be2efb6c-2f83-4baf-8bde-616e19fb08fe	events delete all	events delete	Purges all events from your user. (WARNING: THIS IS PERMANENT)	events
42f64bcc-fc58-4214-88e2-97cff81bf63d	events delete	events	Delete commands for the events system	discord.commands.core
fa234842-45a9-4647-ad7d-3349ddfaede1	events create	events	Creates a new event	events
0dfdeec6-d448-4392-8a38-99c7acd74ebb	events update	events	Updates the date and time of an event	events
97627a4f-4a10-4a33-8eb0-af20fcb9502b	events	None	Commands for Beryl's Events System	discord.commands.core
9014685c-5bd9-4a34-bb40-bba40ada0dde	gws wish one	gws wish	Allows you to wish for one item	gws
ca255a09-e654-4df8-be77-1c749bdfdca2	gws wish multiple	gws wish	Allows you to wish for up to 3 items at once	gws
a43ea994-1d40-44e4-8b3e-27c1f3ee283e	gws wish	gws	Wish for some items	discord.commands.core
16395514-ceb4-4401-9ba0-13ce4999f7eb	gws delete one	gws delete	Deletes one item from your inventory	gws
e695bd04-f651-4199-924a-49438cad3267	gws delete all	gws delete	Deletes all of your items in your GWS inventory	gws
e9050e36-2ed2-4be1-94de-a0c8acff2e17	gws delete	gws	Deletes some stuff from your inv	discord.commands.core
6e6cc782-adaa-499b-9005-11b66cad6a79	gws inv	gws	Accesses your inventory for GWS	gws
94187bdc-4856-456b-9ad4-937680585dd5	gws profile	gws	Gets your GWS profile	gws
c311b607-798a-463d-8370-df0b45608d69	gws	None	Commands for Reina's Genshin Wish Sim	discord.commands.core
3f7cbed2-4df5-43bf-8e5f-885e5df788e8	mangadex search manga	mangadex search	Searches for up to 25 manga on MangaDex	mangadex
6e30eb49-4252-4ec9-94bb-4fa25afaf5f8	mangadex search scanlation	mangadex search	Returns up to 25 scanlation groups via the name given	mangadex
c7f08942-88c9-4dc4-aee1-50f0ebc1f85b	mangadex search author	mangadex search	Returns up to 25 authors and their info	mangadex
ee02f2c4-9e0d-4823-acca-7063227727fe	mangadex search	mangadex	Search for stuff on MangaDex	discord.commands.core
94e35463-ad4d-4c34-a09c-8df2aaf9d1fc	mangadex scanlation	mangadex	Commands for the scanlation section	discord.commands.core
d7035c4c-27bd-4c9d-b9ef-ce94aea8527f	mangadex random	mangadex	Returns an random manga from MangaDex	mangadex
44937ee3-0bfc-485d-b953-0a5708d4d8c3	mangadex	None	Commmands for the MangaDex service	discord.commands.core
e15c51a1-36d5-42a1-b887-a3634e133c4c	mal search anime	mal search	Fetches up to 25 anime from MAL	myanimelist
c142f1d9-9b2d-4804-9893-a59f599beb58	mal search manga	mal search	Fetches up to 25 mangas from MAL	myanimelist
7d01c0b8-9902-4b0b-b844-0f45e2c0a8a4	mal search	mal	Search for anime/manga on MyAnimeList	discord.commands.core
97cf88cf-9104-4cbd-a0cc-ced53daf7aad	mal seasons list	mal seasons	Returns animes for the given season and year	myanimelist
998dda30-1969-4787-864d-71d389706245	mal seasons upcoming	mal seasons	Returns anime for the upcoming season	myanimelist
a38b1238-89d2-42e6-b0a3-6fc528690841	mal seasons	mal	Sub commands for anime seasons	discord.commands.core
b1eef6d1-f38d-4e39-8730-f335ab4e84f6	mal random anime	mal random	Fetches a random anime from MAL	myanimelist
f48d23d5-dd46-4237-819f-e04eb3c7ce86	mal random manga	mal random	Fetches a random manga from MAL	myanimelist
27ab44d1-9895-4382-b9a0-1be89039e466	mal random	mal	Random Anime/Manga Commands	discord.commands.core
b635051d-22b9-423b-9c91-a86b66394d7a	mal user	mal	Returns info about the given user on MAL	myanimelist
f7579100-da73-42d7-9939-688014e5298d	mal	None	Commands for the MyAnimeList/Jikan service	discord.commands.core
78bf2c97-391a-4755-8310-1b1051bc7e15	reddit users info	reddit users	Provides info about a Redditor	reddit
3adcdebf-6cfa-4a5f-9bdf-29a1ee1258c6	reddit users comments	reddit users	Returns up to 25 comments from a given Redditor	reddit
32571ebf-ba98-45d8-8dbd-74be059bb6a7	reddit users	reddit	Subgroup for Reddit Users	discord.commands.core
bff888d7-5b25-4990-8e64-cc9bc5626f1a	reddit search	reddit	Searches on Reddit for Content	reddit
945d7697-9a4a-49ff-9ef0-26859eb7380e	reddit memes	reddit	Gets some memes from Reddit	reddit
bb108044-d95d-4428-bdd0-a0ae97a1a9af	reddit feed	reddit	Returns up to 25 reddit posts based on the current filter	reddit
18fad334-990a-467f-9ff1-634a7c0e4731	reddit egg_irl	reddit	Literally just shows you r/egg_irl posts. No comment.	reddit
6b21a7ea-0fba-4f97-8828-6b3dfad181c0	reddit	None	Commands for Reddit Service	discord.commands.core
f80ef080-8b09-4c47-b58a-862286ba57ec	tenor search multiple	tenor search	Searches for up to 25 gifs on Tenor	tenor
e890dd33-3585-4dc2-a13f-2195b7b56eaf	tenor search one	tenor search	Searches for a single gif on Tenor	tenor
e7f76956-abcc-4801-82df-1324314d9e9d	tenor search suggestions	tenor search	Gives a list of suggested search terms based on the given topic	tenor
e74afdf5-e549-4cba-a19e-26ead3602357	tenor search	tenor	Search Tenor	discord.commands.core
6eb3f20f-5cb7-48ed-9cab-d5e09a68abdd	tenor trending terms	tenor trending	Gives a list of trending search terms on Tenor	tenor
6e702ff3-5c36-44ee-a879-15455cc83ea2	tenor trending	tenor	Trending Tenor	discord.commands.core
0da11c22-ea29-41ce-b60d-ad3c5d6cf0f5	tenor featured	tenor	Returns up to 25 featured gifs from Tenor	tenor
0a52b7c4-cb81-46f2-86fe-4c28d110bf07	tenor random	tenor	Gives out 25 random gifs from Tenor based on given search term	tenor
95d717d5-c7e1-48e7-88ec-c0addb0bbd09	tenor	None	Tenor API commands	discord.commands.core
ea6b6ec1-89f3-4dc9-ad37-19611642b8b7	waifu random one	waifu random	Gets one random waifu pics	waifu
dc10338b-98fd-4f7f-b4c1-91eb634f0a6e	waifu random many	waifu random	Returns many random waifu pics	waifu
363870e7-cf76-4d09-9911-b9eef4cf43e5	waifu random	waifu	Get a random waifu	discord.commands.core
5ab21c6f-c52f-4f5b-b576-4ee92e5c1975	waifu pics	waifu	Returns a random image of a waifu from waifu.pics	waifu
21609a2d-c3b4-486e-ab0a-a0a90bf0f962	waifu	None	Commands to get a ton of waifu stuff	discord.commands.core
ac327317-f2bf-4301-9780-aa8f61372950	utils ffmpegcve	utils	Converts video files to mp4	utility
3040bff5-dcf7-4f35-ba4f-4bb09c317c09	utils hypixel-count	utils	Gets the amount of players in each game server	utility
5a2782ff-d32f-4a99-b066-ceaf5706fed1	utils	None	Util Commands for Reina	discord.commands.core
8b0d5f94-9b49-48a4-b964-4597d977784c	fun random int	fun random	Based on 2 limits, returns a random number	fun
17e8f029-db40-4f41-84f1-c37205f25eb5	fun random dice	fun random	Randomly rolls the dice	fun
41695f37-23cd-4e59-98a0-fa5961e8b1f1	fun random	fun	Random commands	discord.commands.core
53dd0467-26e6-4c87-be7f-6ad017f64414	fun ship	fun	Calculates how much love a person has	fun
0e0ce8e4-39a1-44d3-9416-df756351d007	fun sex	fun	it's a sex calculator	fun
a3380a0e-ac1e-49a7-9c52-e546280b1c4f	fun say	fun	Says something	fun
2a81b60b-74a6-479f-8e99-d9bbf4ef924f	fun laugh	fun	Laughs	fun
c7a6df1f-f6fa-46a4-a1ac-104b19b5b202	fun	None	Some fun commands to use	discord.commands.core
549d576d-0dd8-4354-8bfb-ad38594114c9	jisho search	jisho	Searches for words on Jisho	jisho
c492cfe6-d1d5-461f-aa6c-fd6d4125ead0	jisho	None	Commands for Jisho	discord.commands.core
c5697b50-ea04-496a-b4a1-45ef4d7d47fa	reina uptime	reina	Returns Reina's Uptime	reina
0a331ef6-7a0b-4913-8fb7-9d93af6ab4ee	reina version	reina	Returns Reina's Current Version	reina
7a7a1ecd-902d-4710-82a6-86e11dbfca62	reina ping	reina	Returns Reina's Ping	reina
97fe00dc-f85a-4bfd-a2a8-4baa6acd7e30	reina help	reina	The Help Command for Reina	reina
cfb0f29f-ceda-42ea-80f5-c3c7b32b68e3	reina platform	reina	Returns platform info about Reina	reina
24c22614-be2b-4b89-8833-aa8ee7583a8d	reina	None	Utility Commands for Reina	discord.commands.core
\.


--
-- Name: help_data help_data_pkey; Type: CONSTRAINT; Schema: public; Owner: Reina
--

ALTER TABLE ONLY public.help_data
    ADD CONSTRAINT help_data_pkey PRIMARY KEY (uuid);


--
-- PostgreSQL database dump complete
--
