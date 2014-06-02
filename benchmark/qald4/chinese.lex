// TO BE
// ------

	是  || (S DP[subject] (VP V:'是' DP[object]))  || <x, l1, t, [ l1:[ | ], l2:[ | x=y ] ], [ (l3,x,subject,<<e,t>,t>), (l4,y,object,<<e,t>,t>) ], [  l3<l1, l4<l1, l2<scope(l3), l2<scope(l4) ],[]>
	是  || (S DP[subject] (VP V:'是' ADJ[comp]))   || <x, l1, t, [ l1:[ | x=y ]], [ (l2,x,subject,<<e,t>,t>), (l3,y,comp,<e,t>) ], [  l2=l1, l3=l2 ],[]>
	是什么 || (NP NP* (S C:'which' (VP V:'is' DP[object]))) || <x, l1, t, [ l1:[ | x=y ] ], [ (l2,y,object,<<e,t>,t>) ], [ l2=l1 ],[]>

	是否有 | 有没有  || (S V:'is' C:'there' DP[dp])  || <x, l1, t, [ l1:[ | ] ], [ (l2,x,dp,<<e,t>,t>) ], [ l2=l1 ],[]>

// TO BE: YES/NO QUESTIONS

	是 | 么 | 吗 || (S (VP V:'is' DP[subject] DP[object]))   || <x, l1, t, [ l1:[ | ], l2:[ | x=y ] ], [ (l3,x,subject,<<e,t>,t>), (l4,y,object,<<e,t>,t>) ], [  l3<l1, l4<l1, l2<scope(l3), l2<scope(l4) ],[]>
	是 | 么 | 吗 || (S (VP V:'is' DP[subject] ADJ[comp]))    || <x, l1, t, [ l1:[ | x=y ]], [ (l2,x,subject,<<e,t>,t>), (l3,y,comp,<e,t>) ], [  l2=l1, l3=l2 ],[]>

// IMPERATIVES
// ---------------------

	给我 || (S (VP V:'give' (DP N:'me') DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
	说出 || (S (VP V:'name' DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
//	give me all || (S (VP V:'give' (DP N:'me') DET:'all' DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
//	name all || (S (VP V:'name' DET:'all' DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
	举例 || (S (VP V:'show' (DP N:'me') DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
	列举 || (S (VP V:'show' DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>
	列出 || (S (VP V:'list' DP[object])) || <x,l1,t,[ l1:[ ?x | x=y ] ],[ (l2,y,object,<<e,t>,t>) ],[ l1=l2 ],[]>


// DETERMINER
// ----------

	一个  || (DP DET:'a' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] SOME y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	所有 || (DP DET:'all' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] EVERY y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	每个 || (DP DET:'every' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] EVERY y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
//?	no || (DP DET:'no' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] NO y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	每一个 || (DP DET:'each' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] EVERY y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	最多 || (DP DET:'the' ADJ:'most' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] THEMOST y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	最少 || (DP DET:'the' ADJ:'least' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] THELEAST y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	一些 || (DP DET:'a' ADJ:'few' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] AFEW y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	某些 || (DP DET:'some' NP[noun]) || <x, l1, <<e,t>,t>, [ l1:[ x | ] ], [ (l2,x,noun,<e,t>) ], [ l2=l1 ],[]>
	哪些 || (DP DET:'which' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ ?y | ] ], [ (l2,y,noun,<e,t>) ], [ l2=l1 ],[]>
	什么 || (DP DET:'what' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ ?y | ] ], [ (l2,y,noun,<e,t>) ], [ l2=l1 ],[]>
	多少 || (DP DET:'many' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] MANY y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
	至少 || (DP DET:'at' DET:'least' NUM[num] NP[noun]) || <y,l1,<<e,t>,t>,[l1:[ y | count_greatereq(y,x) ]],[(l2,y,noun,<e,t>),(l3,x,num,e)],[ l1=l2, l2=l3 ],[]>
	至多 || (DP DET:'at' DET:'most' NUM[num] NP[noun]) || <y,l1,<<e,t>,t>,[l1:[ y | count_lesseq(y,x) ]],[(l2,y,noun,<e,t>),(l3,x,num,e)],[ l1=l2, l2=l3 ],[]>
	正好 || (DP DET:'exactly' NUM[num] NP[noun]) || <y,l1,<<e,t>,t>,[l1:[ y | count_eq(y,x) ]],[(l2,y,noun,<e,t>),(l3,x,num,e)],[ l1=l2, l2=l3 ],[]>

	其他 || (NP ADJ:'other' NP*) || <x,l1,<e,t>,[ l1:[ | ] ], [],[],[]>
	总共 || (NP ADJ:'total' NP[np]) || <s,l1,<e,t>,[ l1:[ ?s | sum(a,x,s) ] ], [ (l2,x,np,<e,t>) ],[ l2=l1 ],[]>

	最少 || (ADJ DET:'least' ADJ*) || <x,l1,<e,t>,[ l1:[ | minimum(a,x,x) ] ], [],[],[]>

  	有多少  || (DET DET:'how' DET:'many')  || <x,l1,e, [ l1:[ ?x | ] ], [],[],[]>
  	多少次 | 几次 || (DP DET:'how' DET:'often') || <x,l1,<<e,t>,t>, [ l1:[ | count(x) ] ], [],[],[]>
	一个  || (DET DET:'a') || <x,l1,e, [ l1:[ x |] ], [],[],[]>
	哪个 || (DET DET:'which') || <x,l1,e, [ l1:[ ?x |] ], [],[],[]>
	最多 || (DET DET:'the' DET:'most') || <y, l1, e, [ l1:[ | l2:[ y | ] THEMOST y l3:[|] ] ], [], [],[]>
	最少 || (DET DET:'the' DET:'least') || <y, l1, e, [ l1:[ | l2:[ y | ] THELEAST y l3:[|] ] ], [], [],[]>

    // NECESSARY "CHEAT"
	最高 || (NP ADJ:'highest' NP*) || <x, l1, e, [ l1:[ j | SLOT_high(x,j), maximum(j) ] ],[],[],[ SLOT_high/PROPERTY/height ]> ;; <x, l1, e, [ l1:[ | maximum(x) ] ], [], [],[]>

	// COUNT
	多于 | 以上 | 超过 || (DP DET:'more' DET:'than' NUM[num] NP[np]) || <y,l1,<<e,t>,t>,[ l1:[ y,c | count_greater(y,z) ] ],[(l2,y,np,<e,t>),(l3,z,num,e)],[l2=l1,l3=l1],[]> ;; <y,l1,<<e,t>,t>,[ l1:[ y | greater(y,z) ] ],[(l2,y,np,<e,t>),(l3,z,num,e)],[l2=l1,l3=l1],[]>
	少于 || (DP DET:'less' DET:'than' NUM[num] NP[np]) || <y,l1,<<e,t>,t>,[ l1:[ y,c | count_less(y,z) ] ],[(l2,y,np,<e,t>),(l3,z,num,e)],[l2=l1,l3=l1],[]> ;; <y,l1,<<e,t>,t>,[ l1:[ y | less(y,z) ] ],[(l2,y,np,<e,t>),(l3,z,num,e)],[l2=l1,l3=l1],[]>

	// HOW
	// how || (DP DET:'how' ADJ[adj]) || <x,l1,<<e,t>,t>,[ l1:[?x,|] ],[ (x,l2,adj,<e,t>) ],[l2=l1],[]>


// EMPTY STUFF
// ------------

	也 || (VP ADV:'also' VP*) || <x,l1,t,[ l1:[|] ],[],[],[]>
	也 || (DP ADV:'also' DP*) || <x,l1,<<e,t>,t>,[ l1:[|] ],[],[],[]>

//	with || (NP NP* (PP P:'with' DP[dp])) || <x,l1,<e,t>,[ l1:[| empty(x,y) ] ],[(l2,y,dp,<<e,t>,t>)],[l2=l1],[]>
//      of   || (NP NP* (PP P:'of' DP[dp])) || <x,l1,<e,t>,[ l1:[| empty(x,y) ] ],[(l2,y,dp,<<e,t>,t>)],[l2=l1],[]>

	人 || (NP N:'people') || <x,l1,<e,t>,[ l1:[|] ],[],[],[]>
    还 || (ADJ ADJ:'still' ADJ*) || <x,l1,<e,t>,[l1:[|]],[],[],[]>


// WH WORDS
// --------

	什么     || (DP WH:'what')      || <x, l1, <<e,t>,t>, [ l1:[ ?x | ] ], [], [], []>
	哪些 | 哪个    || (DP WH:'which')     || <x, l1, <<e,t>,t>, [ l1:[ ?x | ] ], [], [], []>
	多少 | 总和 || (DP WH:'how' ADJ:'many' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ | l2:[ y | ] HOWMANY y l3:[|] ] ], [ (l4,y,noun,<e,t>) ], [ l4=l2 ],[]>
    多少 | 总和　|| (DP WH:'how' ADJ:'many' NP[noun]) || <y, l1, <<e,t>,t>, [ l1:[ ?y | ] ], [ (l4,y,noun,<e,t>) ], [ l4=l1 ],[]>
	谁      || (DP WH:'who')       || <x, l1, <<e,t>,t>, [ l1:[ ?x | ] ], [], [], []>
	什么时候 | 什么时间 | 哪年     || (S WH:'when' S[s])  || <x, l1, t, [ l1:[ ?x | SLOT_p(y,x) ] ], [(l2,y,s,t)], [l2=l1], [ SLOT_p/PROPERTY/date ]>
	什么时候 | 什么时间 | 哪年    || (DP WH:'when')      || <y, l1, <<e,t>,t>, [ l1:[ ?x | SLOT_p(y,x) ] ], [], [], [ SLOT_p/PROPERTY/date ]>
	哪 | 哪里    || (S WH:'where' S[s]) || <x, l1, t, [ l1:[ ?x | SLOT_p(y,x) ] ], [(l2,y,s,t)], [l2=l1], [ SLOT_p/PROPERTY/place ]>
	哪 | 哪里    || (DP WH:'where')     || <y, l1, <<e,t>,t>, [ l1:[ ?x | SLOT_p(y,x) ] ], [], [], [ SLOT_p/PROPERTY/place ]>
	在哪里 || (DP WH:'where' (PP P:'in' DP[dp])) || <y, l1, <<e,t>,t>, [ l1:[ ?x | SLOT_p(y,x), SLOT_in(x,z) ] ], [(l2,z,dp,<<e,t>,t>)], [l2=l1], [ SLOT_p/PROPERTY/place ]>


// NEGATION
// --------

   不 || (ADJ NEG:'not' ADJ*) || <x,l2,t,[ l1:[ | NOT l2:[|] ] ],[],[],[]>
   不 || (VP NEG:'not' VP*) || <x,l2,t,[ l1:[ | NOT l2:[|] ] ],[],[],[]>


// COORDINATION
// ------------

	和 || (S S* CC:'和' S[s]) || <x,l1,t,[l1:[|]],[(l2,y,s,t)],[l1=l2],[]>
	和 || (DP DP* CC:'和' DP[dp]) || <x,l1,<<e,t>,t>,[l1:[|]],[(l2,y,dp,<<e,t>,t>)],[l1=l2],[]>
	和 || (NP NP* CC:'和' NP[np]) || <x,l1,<e,t>,[l1:[|x=y]],[(l2,y,np,<e,t>)],[l1=l2],[]>
	和 || (VP VP* CC:'和' VP[vp]) || -
	和 || (ADJ ADJ* CC:'和' ADJ[adj]) || -

	以及 || (NP NP* CC:'以及' NP[np]) || <x,l1,<e,t>,[l1:[|]],[(l2,y,np,<e,t>)],[l1=l2],[]>

	或 || (S S* CC:'或' S[2]) || -
	或 || (DP DP* CC:'或' DP[2]) || -
	或 || (NP NP* CC:'或' NP[2]) || -
	或 || (VP VP* CC:'或' VP[2]) || -
	或 || (ADJ ADJ* CC:'或' ADJ[2]) || -


// EXISTENTIAL
// -----------

	there || (DP (NP EX:'there')) || <x,l1,<<e,t>,t>,[l1:[|]],[],[],[]>
// NUMBERS (1-10)
// ---------------------

	一   || (NP NUM:'一' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,1)]],[],[],[]>
	二   || (NP NUM:'二' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,2)]],[],[],[]>
	三   || (NP NUM:'三' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,3)]],[],[],[]>
	四   || (NP NUM:'四' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,4)]],[],[],[]>
	五   || (NP NUM:'五' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,5)]],[],[],[]>
	六   || (NP NUM:'六' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,6)]],[],[],[]>
	七   || (NP NUM:'七' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,7)]],[],[],[]>
	八   || (NP NUM:'八' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,8)]],[],[],[]>
	九   || (NP NUM:'九' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,9)]],[],[],[]>
	十   || (NP NUM:'十' NP*)   || <x,l1,<e,t>,[l1:[x|count(x,10)]],[],[],[]>

	一   || (NP NUM:'一' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,1)]],[],[],[]>
	二   || (NP NUM:'二' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,2)]],[],[],[]>
	三   || (NP NUM:'三' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,3)]],[],[],[]>
	四   || (NP NUM:'四' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,4)]],[],[],[]>
	五   || (NP NUM:'五' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,5)]],[],[],[]>
	六   || (NP NUM:'六' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,6)]],[],[],[]>
	七   || (NP NUM:'七' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,7)]],[],[],[]>
	八   || (NP NUM:'八' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,8)]],[],[],[]>
	九   || (NP NUM:'九' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,9)]],[],[],[]>
	十   || (NP NUM:'十' NP*)   || <x,l1,<e,t>,[l1:[x|equal(x,10)]],[],[],[]>