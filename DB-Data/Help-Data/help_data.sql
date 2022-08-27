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
6fe98d89-6c1f-45ba-b04e-6a8da0cf5bf5	anilist search anime	anilist search	Searches for up to 25 animes on AniList	anilist
02fe3e0e-b921-4cf1-88a4-d2d57e4f8f6d	anilist search characters	anilist search	Searches up to 25 anime characters on AniList	anilist
87d35cd1-bea2-4ed6-af74-f633e62c40c0	disquest rank local	disquest rank	Displays the most active members of your server!	disquest
f6aa6464-6214-49ee-9c54-d56cd4883da2	disquest init	disquest	Initializes the database for DisQuest!	disquest
f7876af2-7a3b-4679-9c5b-567cfbfab876	events view past	events view	View all of your past events	events
0bbe35c7-072d-44c8-840d-715b7add004f	events delete all	events delete	Purges all events from your user. (WARNING: THIS IS PERMANENT)	events
c3f8bbdb-b962-47c9-af64-84b4952ee2d8	events	None	Commands for Beryl's Events System	discord.commands.core
1f9cadc1-b6ca-4278-82dd-35a10c7c1cb4	gws delete one	gws delete	Deletes one item from your inventory	gws
f81e226a-85f0-4494-b17d-83a4a88835e3	gws profile	gws	Gets your GWS profile	gws
faa3ccf3-7f21-41b8-a796-0e92d82fda90	mangadex search scanlation	mangadex search	Returns up to 25 scanlation groups via the name given	mangadex
4989288c-eccb-4637-9d88-1bc5660a2394	mangadex random	mangadex	Returns an random manga from MangaDex	mangadex
771adbdc-d97f-4ea3-b0b2-fcf8d85d43a7	mal search	mal	Search for anime/manga on MyAnimeList	discord.commands.core
7173d62b-69ff-4bf2-b03a-6f38e515d178	mal seasons	mal	Sub commands for anime seasons	discord.commands.core
58a2707a-6a1c-4bc0-b96e-d19cb0721500	mal random	mal	Random Anime/Manga Commands	discord.commands.core
9a6bc000-312e-4272-98ef-ec289d7537ff	tenor search multiple	tenor search	Searches for up to 25 gifs on Tenor	tenor
e2937e9e-3417-42f7-8fa8-396280ef752e	tenor search	tenor	Search Tenor	discord.commands.core
a2729408-40f4-4b33-b1e4-b42b9d3d0508	tenor featured	tenor	Returns up to 25 featured gifs from Tenor	tenor
9ce4a5d6-ea10-43d5-af4a-3d75a39f83f6	waifu random one	waifu random	Gets one random waifu pics	waifu
61ce161e-83d8-4ccf-bae3-a670fb3f047c	waifu pics	waifu	Returns a random image of a waifu from waifu.pics	waifu
eea040ce-2d33-46b3-a550-51fd81b73d03	fun random dice	fun random	Randomly rolls the dice	fun
03293c2c-f512-4c28-bc6f-6a02efc255d5	fun sex	fun	it's a sex calculator	fun
73408d0b-22b1-4110-b238-50bb3a4506ab	fun	None	Some fun commands to use	discord.commands.core
ea367430-7c88-41e4-8008-edc736bfc3a5	reina uptime	reina	Returns Reina's Uptime	reina
73afff77-9f88-4e5c-b354-f83d406dfd4e	reina help	reina	The Help Command for Reina	reina
7982eccc-51eb-4c00-beb9-dcfc48874920	utils hypixel-count	utils	Gets the amount of players in each game server	utility
166d8f20-185b-412c-ae00-bce293bf6b71	anilist search manga	anilist search	Searches for up to 25 mangas on AniList	anilist
bd099de6-a3b5-4ed7-a115-bc7bc97f1b19	anilist search actors	anilist search	Searches for up to 25 voice actors or staff that have worked on an anime and/or its characters	anilist
dfa5670e-a818-48a5-9db2-051d605ebdae	disquest rank global	disquest rank	Displays the most active members of all servers that this bot is connected to!	disquest
8587e39c-e47c-40a9-aa22-bd6630039536	disquest	None	Commands for Disquest	discord.commands.core
18475ff7-310b-4352-b6ad-f5f881dc63fe	events view countdown	events view	Checks how much days until an event will happen and pass	events
ea1296ef-69e6-4469-9cd1-0162a018c6cd	events delete	events	Delete commands for the events system	discord.commands.core
bdcedb36-ff33-45ec-89e2-62eea8df403c	gws wish one	gws wish	Allows you to wish for one item	gws
038aab60-0488-4937-816a-55fc4925ae5d	gws delete all	gws delete	Deletes all of your items in your GWS inventory	gws
ac6b1e75-e4e2-4af8-96ab-a510c8349473	gws	None	Commands for Reina's Genshin Wish Sim	discord.commands.core
6147005c-7bf6-4f05-824c-4c6ca118e4d1	mangadex search author	mangadex search	Returns up to 25 authors and their info	mangadex
feb6ac29-5ec2-49b6-ae75-19eef708e0a0	mangadex	None	Commmands for the MangaDex service	discord.commands.core
a44dad22-096a-4116-a28e-6d65871f0821	mal seasons list	mal seasons	Returns animes for the given season and year	myanimelist
db29e60e-cf9a-4c11-9cf7-a70a88a56465	mal random anime	mal random	Fetches a random anime from MAL	myanimelist
d46a8619-25f9-4460-ba1a-5fecc946b086	mal user	mal	Returns info about the given user on MAL	myanimelist
fc0a28d3-e490-4fbb-853d-08558a4f4ce0	tenor search one	tenor search	Searches for a single gif on Tenor	tenor
fb39b2ae-c20e-460b-a073-1fcd46fb582d	tenor trending terms	tenor trending	Gives a list of trending search terms on Tenor	tenor
5da38ea5-6fdf-4513-b447-a4b774e19e69	tenor random	tenor	Gives out 25 random gifs from Tenor based on given search term	tenor
377649b3-0061-4076-8fdf-7c5ab21759bf	waifu random many	waifu random	Returns many random waifu pics	waifu
2b36ab5f-d187-48ad-b3a4-8b62e7c0ce99	waifu	None	Commands to get a ton of waifu stuff	discord.commands.core
5918863c-b892-4e05-aa8d-9e251969b95f	fun random	fun	Random commands	discord.commands.core
7113e849-b2b6-4271-82a9-fe90b5466416	fun say	fun	Says something	fun
13f3752e-b2da-4972-8526-b56b7870401c	jisho search	jisho	Searches for words on Jisho	jisho
d9e288de-ad85-4273-ba37-d9d90878cf2e	reina version	reina	Returns Reina's Current Version	reina
1b025023-6f01-4ae9-93df-336be0aa293a	reina platform	reina	Returns platform info about Reina	reina
3658fdd8-4326-453c-8882-f2a5305a5b6f	utils	None	Util Commands for Reina	discord.commands.core
37b9da4b-7aca-4618-ae72-102857f318c0	anilist search tags	anilist search	Searches up to 25 animes and mangas based on the given tag	anilist
7aefee60-df20-48d8-990e-eb1bb6438fea	anilist search	anilist	Search for anime on AniList	discord.commands.core
e94ddb57-22de-4b98-bc5b-0d26ddb2a07f	disquest rank	disquest	Commands for Disquest	discord.commands.core
d17fb54d-2175-4fdd-9fc9-005d05d4c52a	events view all	events view	Views all of your past and upcoming events	events
bb2dd5a9-afeb-45e5-9280-30498f807318	events view	events	View the events	discord.commands.core
0c72bea3-19be-4b13-bd64-d42f3e95172f	events create	events	Creates a new event	events
390ec6e0-401c-40d9-b081-4a67ddc80565	gws wish multiple	gws wish	Allows you to wish for up to 3 items at once	gws
4fc50d23-d43c-4eb0-bf45-b43757769a0c	gws delete	gws	Deletes some stuff from your inv	discord.commands.core
8864c661-bb35-433d-9a98-124842327621	mangadex search	mangadex	Search for stuff on MangaDex	discord.commands.core
97e5c49a-9db7-4d53-9b06-11446c34f36e	mal search anime	mal search	Fetches up to 25 anime from MAL	myanimelist
2ab58895-7b83-4f36-adad-44c43f9f698b	anilist search users	anilist search	Provides up to 25 users from the given username	anilist
a40656f7-159a-4a70-9c68-80807e6d8c87	anilist	None	Commands for AniList service	discord.commands.core
543119df-1938-4a36-b436-50e15316716b	disquest mylvl	disquest	Displays your activity level!	disquest
abb0ae6e-4618-4d3f-927e-c2e63eb5e176	events view upcoming	events view	View all of your upcoming events	events
005b1412-96d0-4e82-89c3-0a45e0775923	events delete one	events delete	Deletes one event from your list of events	events
e7088954-b689-4f05-9cc8-14f972ab9445	events update	events	Updates the date and time of an event	events
313039a0-6e2e-4ba3-8370-ebff5e95fdcc	gws wish	gws	Wish for some items	discord.commands.core
0a4ca5cb-d376-4345-a9d5-a28c578524a0	gws inv	gws	Accesses your inventory for GWS	gws
cbc3dd52-d92b-4e40-8c65-5d9f9650109f	mangadex search manga	mangadex search	Searches for up to 25 manga on MangaDex	mangadex
01f07787-06af-413d-868c-e46721e573a1	mangadex scanlation	mangadex	Commands for the scanlation section	discord.commands.core
cc24b60d-c372-4b68-a909-f93871d5b274	mal search manga	mal search	Fetches up to 25 mangas from MAL	myanimelist
e8839cd4-0ddf-486d-b7ff-ba5317375d3e	mal seasons upcoming	mal seasons	Returns anime for the upcoming season	myanimelist
05822bce-999d-4612-9ed9-fab638efca53	mal random manga	mal random	Fetches a random manga from MAL	myanimelist
a705998c-bbfd-45db-8cba-bd982abcace8	mal	None	Commands for the MyAnimeList/Jikan service	discord.commands.core
a031de8e-a475-456c-8ea9-aa90995cff41	tenor search suggestions	tenor search	Gives a list of suggested search terms based on the given topic	tenor
2efa8ca9-6af1-4396-a899-ec62dac0f6a8	tenor trending	tenor	Trending Tenor	discord.commands.core
034bc0a4-9608-474e-b44c-e7f2d442e8f5	tenor	None	Tenor API commands	discord.commands.core
5f920485-a999-4ad8-83f4-1cc872226b05	waifu random	waifu	Get a random waifu	discord.commands.core
ba550e2c-2f3e-4dc7-a0a0-43758cb51588	fun random int	fun random	Based on 2 limits, returns a random number	fun
7ff7cb82-bd5a-4a74-882e-5b4b1e1df6cd	fun ship	fun	Calculates how much love a person has	fun
b03b5dd8-64fa-4501-82e6-08f4184f21f1	fun laugh	fun	Laughs	fun
67679bb0-4d52-4bb0-908c-c8112c2275f0	jisho	None	Commands for Jisho	discord.commands.core
3d9995ca-218a-49ae-bebc-dc02a55eb7ad	reina ping	reina	Returns Reina's Ping	reina
65f64064-82b6-4778-bd0c-fe391c6f51c2	reina	None	Utility Commands for Reina	discord.commands.core
ca34524a-62f2-4dc0-ae2f-1ca50770b086	utils ffmpegcve	utils	Converts video files to mp4	utility
\.


--
-- Name: help_data help_data_pkey; Type: CONSTRAINT; Schema: public; Owner: Reina
--

ALTER TABLE ONLY public.help_data
    ADD CONSTRAINT help_data_pkey PRIMARY KEY (uuid);


--
-- PostgreSQL database dump complete
--

