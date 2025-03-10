

#####  The Crop Journal 11 (2023) 247–257  Contents lists available at ScienceDirect  The Crop Journal 
journal homepage: www.keaipublishing.com/en/journals/the-crop-journal/ 
Time-resolved multiomics analysis of the genetic regulation of maize kernel moisture 
Jianzhou Qu a,b, Shutu Xu a,b,⇑, Xiaonan Gou a,b, Hao Zhang a,b, Qian Cheng a,b, Xiaoyue Wang a,b, Chuang Ma a,c,⇑, Jiquan Xue a,b,⇑ a 
The Key Laboratory of Biology and Genetic Improvement of Maize in Arid Area of Northwest Region, Northwest A&F University, Yangling 712100, Shaanxi, China b 
Maize Engineering & Technology Research Centre, College of Agronomy, Northwest A&F University, Yangling 712100, Shaanxi, China c 
State Key Laboratory of Crop Stress Biology for Arid Areas, Center of Bioinformatics, College of Life Sciences, Northwest A&F University, Yangling 712100, Shaanxi, China a r t i c l e i n f oa b s t r a c t 
Article history: Maize kernel moisture content (KMC) at harvest greatly affects mechanical harvesting, transport and 
Received 2 March 2022storage. KMC is correlated with kernel dehydration rate (KDR) before and after physiological maturity. 
Revised 13 April 2022KMC and KDR are complex traits governed by multiple quantitative trait loci (QTL). Their genetic archi- Accepted 24 April 2022 
 tecture is incompletely understood. We used a multiomics integration approach with an association Available online 7 June 2022 
 panel to identify genes influencing KMC and KDR. A genome-wide association study using time-series 
 KMC data from 7 to 70 days after pollination and their transformed KDR data revealed respectively 98 Keywords: 
 and 279 loci significantly associated with KMC and KDR. Time-series transcriptome and proteome data- Maize Kernel moisture 
 sets were generated to construct KMC correlation networks, from which respectively 3111 and 759 mod- 
Kernel dehydration rateule genes and proteins were identified as highly associated with KMC. Integrating multiomics analysis, 
GWAS several promising candidate genes for KMC and KDR, including Zm00001d047799 and 
Multiomics Zm00001d035920, were identified. Further mutant experiments showed that Zm00001d047799, a gene 
 encoding heat shock 70 kDa protein 5, reduced KMC in the late stage of kernel development. Our study 
 provides resources for the identification of candidate genes influencing maize KMC and KDR, shedding 
 light on the genetic architecture of dynamic changes in maize KMC. 
Ó 2022 Crop Science Society of China and Institute of Crop Science, CAAS. Production and hosting by 
 Elsevier B.V. on behalf of KeAi Communications Co., Ltd. This is an open access article under the CC BY-NC- ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/). 
1. Introductionmaturity, in which KMC is influenced by external environmental 
 factors in addition to genetic factors [4,5]. Kernel dehydration rate 
 Maize (Zea mays L.) is a food and fodder crop worldwide. Kernel (KDR) also determines KMC at harvest, and maize varieties with 
moisture content (KMC) affects maize production and breeding.fast KDR before and after physiological maturity generally have 
High KMC at harvest increases the risk of ear sprouting, ear rot,lower KMC at harvest [6,7]. Both KMC and KDR are closely associ- 
and plant lodging, thus affecting the harvesting and safe storageated with kernel composition (including sugars, water-soluble 
of maize kernels, especially in short- to mid-season growing areas polysaccharides, and some hydrophobic compounds) [8,9] and var- 
affected by environmental factors such as temperature, rainfall, ious agronomic traits (including kernel row number, ear length and 
and relative humidity [1–3]. Reducing KMC at harvest has becomediameter, pericarp thickness, and husk length and tightness) [10– 
a target of maize breeding and biotechnology-assisted15]. Maize KMC and KDR are quantitative traits, making the iden- improvement. tification of their genetic basis difficult. 
 KMC at harvest is determined by two phases: the first phase isIn association studies aimed at identifying the genetic basis of 
before physiological maturity, in which KMC is associated mainly KMC and KDR, multiple quantitative trait loci (QTL) for maize 
with accumulation of dry matter via kernel filling and regulated KMC and KDR have been detected in diverse populations by pheno- 
mainly by genetic factors. The second phase is after physiological type–genotype association analysis [1,3,16–28]. However, no QTL 
 have been fine-mapped or even cloned, owing to technical limita- 
 tions and the inherent complexity of KMC and KDR. Further inves- 
⇑ Corresponding authors. tigations are needed to elucidate the genetic basis of KMC and KDR 
 E-mail addresses: xjq2934@163.com (J. Xue), chuangma2006@gmail.com (J. Ma), and to perform gene-based breeding to improve maize KMC. shutuxu@nwafu.edu.cn (S. Xu). https://doi.org/10.1016/j.cj.2022.04.017 
2214-5141/Ó 2022 Crop Science Society of China and Institute of Crop Science, CAAS. Production and hosting by Elsevier B.V. on behalf of KeAi Communications Co., Ltd. 
This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
 A genome-wide association study (GWAS), a high-resolutionTwo methods were used to calculate KDR: KDR1, method, provides an opportunity to methodically investigate the 
genetic architecture of complex traits and identify beneficial alleles KDR (%) = [(KMCn  KMCnþ7 )/7]  100%. ð2Þ based on high diversity and rapid linkage disequilibrium (LD) 
 where n is the nth sampling date, and KDR2, the area under the dry decay [29,30]. For maize KMC and KDR, several studies [28,31–  down curve (AUDDC): 
33] have employed GWAS to identify favorable alleles. These stud- 
ies showed the promise of linking GWAS loci to genes associated X n1 
with KMC and KDR. With the development of next-generationAUDDC ¼½ðci þ ciþ1 Þ=2ðt iþ1  ti Þ ð3Þ 
sequencing technologies, individual omics data provide comple- i mentary support so that integrating multiomics data is expected 
 where n is the number of assessments, c is the mean KMC, i is the to strengthen the signal for pinpointing genes associated with 
 ith sample, and t is the pollination date (7, 14, 21, 28, 35, 42, 49, 
KMC and KDR. At a different omics level, multiomics data for indi-  56, 63 and 70 DAP) [36]. 
vidual genes are further amplified when multiple genes are consid- A mixed linear model was built by fitting intercept as a fixed 
ered together, particularly given the polygenicity of KMC and KDR.  effect and genotype and year as random effects in SAS 8.1 (SAS 
 The object of the present study was to identify gene sets influ- 
 Inc., Cary, NC, USA). The best linear unbiased prediction (BLUP) encing KMC and KDR by identifying candidate genes for KMC and 
 value for each maize inbred line was calculated. Broad-sense heri- KDR using large-scale GWAS and temporal transcriptomic and pro-  tability (H2) was calculated as follows: teomic atlases. In promising candidate gene sets, we cloned and 
identified ZmHSP5, which encodes a heat shock 70 kDa protein 5.d2 
These results confirm and greatly expand our previous understand-H2 ¼  2 G 2  ð4Þ  dG þ dE =n 
ing of the genetic architecture of maize KMC and KDR and provide 
a resource for future research on the molecular mechanisms ofwhere d2G is genotypic variance; d2E is residual variance; and n is the reducing maize KMC at harvest. 
 number of years [37]. All data from all developmental time points of 
 each year and BLUP were used for subsequent analyses, including 
2. Materials and methods 30 KMC, 135 KDR1, and 135 KDR2 traits. 
2.1. Plant materials and field design 
 2.3. DNA sample preparation, genotyping, and filtering An association mapping panel (named AM212) of 212 maize Fresh young leaves were collected 3 weeks after sowing and inbred lines comprised 197 inbred lines from the Shaan A (41)  quickly frozen in liquid nitrogen. Total DNA was manually and Shaan B (1 5 6) groups [34] and 15 inbred lines collected  extracted by the cetyltrimethylammonium bromide method [38]. domestically and abroad. Trials were performed at the maize  Total DNA was quantified with a NanoDrop ND-2000 (Thermo 
breeding testing station of Northwest A&F University in Yangling,  Fisher Scientific, Waltham, MA, USA) and 1% agarose gel elec- 
Shaanxi province (108°050 N, 34°320 E) in 2018 and 2019. The field 
 trophoresis. DNA samples that passed the quality check and then experiment followed a randomized complete block design with  performed genotype detection using the Affymetrix maize 6H90K two replications. Each inbred line was planted in 4 rows with 
 Chip (Beijing Compass Biotechnology Co., Ltd., Beijing, China). A 
row lengths of 4.5 m and row spacing of 0.6 m. The planting den-  total of 73,006 markers were generated, and SNPs were filtered 
sity was 75,000 plants per hectare and standard irrigation and fer-  using a missing rate  20% and minor allele frequency tilization management practices were used throughout the  (MAF)  5% using PLINK [39]. Missing genotypes were imputed developmental period. An ethyl methanesulfonate (EMS) mutant  with Beagle 5.1 [40] with default parameters. of Zm00001d047799 (EMS4-0be358) was ordered from the Maize EMS induced Mutant Database (https://elabcaas.cn/memd/public/ 
index.html#) [35], and was backcrossed once with B73 and then2.4. Genome-wide association analysis selfed once. The mutation site was genotyped by sequencing with 
primers listed in Table S1. GWAS was performed using a mixed linear model implemented  in GEMMA 0.98.4 [41]. PCA was performed using BLUP values with 
2.2. Phenotype data collection and analysisthe FactoMineR and factoextra packages [42]. KMC, KDR1, and KDR2 
 data from all years, BLUP data, and the first 10 PCs for all traits 
The ears of all maize inbred lines were bagged before silk emer- were subjected to GWAS. The number of PCs of the associated pop- 
gence. To ensure that all ears of AM212 were synchronized with ulation was estimated with GCTA [43]. A neighbor-joining tree was 
respect to developmental stage to minimize any environmental constructed using MEGA-X 10.0.5 [44] and visualized with iTOL 
influence on kernel dehydration, we performed self-pollination or(https://itol.embl.de). The Bonferroni-corrected threshold (0.05/ 
sib pollination for three days and marked the date of pollinationthe number of effective SNPs) was shown to be too stringent 
on the bag. KMC was measured at 10 successive stages (7, 14, 21, [45]. Accordingly, a P-value of 1.49  105 (P = 1/N, N = 67,076) 
28, 35, 42, 49, 56, 63 and 70 DAP). Three well-pollinated ears pol-was adopted as a threshold for declaring a significant association 
linated on the same day were collected in each plot and threshed by the adjusted Bonferroni method [46]. The mean LD decay dis- 
by hand immediately after collection. One hundred kernels were tance was calculated using PLINK 1.90b6.25 and a value of 
excised from each ear with a scalpel and placed in an aluminum r2 < 0.2 was considered to indicate linkage. The mean r2 for all 
box (80 mm diameter  50 mm height). After sampling, kernelchromosomes was estimated at 200 kb, when the value of the 
fresh weight (W1) was measured with a 0.001 g digital scale andcutoff for r2 was set to 0.1. For each significant SNP detected, a 
each box was labeled with the date, sample name, and number200-kb region flanking the SNP was searched for candidate genes. 
and then placed in an oven. The samples were heated at 105 °CThe physical location of the SNPs was identified based on the maize 
for 30 min and then dried at 70 °C to constant weight (W2). KMCgenomic sequence version 3.0 (ZmB73_RefGen_v3; https:// 
was calculated as. www.maizesequence.org), and all v3 candidate gene IDs were con-  verted to v4 gene IDs by the MaizeGDB database (https:// KMC (%) = [(W1  W2)/W1]  100% ð1Þwww.maizegdb.org).  248  


##### J. Qu, S. Xu, X. Gou et al.The Crop Journal 11 (2023) 247–257 
2.5. RNA-seq and data analysis developmental time points were used for module construction. 
 All gene and protein abundances were normalized. Pearson’s cor- 
Eight maize inbred lines were selected from fast-dehydration relation coefficients (PCCs) for each gene–gene and protein–pro- 
types (KB182, KA225, KA105, and KB035, designated FD1–FD4) tein comparison were calculated, and an adjacency matrix of 
and slow-dehydration types (PH6WC, KB020, KA327, and 91227,the connection strengths was constructed. The best power b 
designated SD1–SD4). The kernels of these inbred lines were sam- was optimized to adjust the scale-free property of the coexpres- 
pled by manual dissection at 21, 28, 35, 42, 49, and 56 DAP in 2018, sion network and the sparsity of connections between genes or 
frozen immediately in liquid nitrogen, and stored at  80 °C. Threeproteins. Highly similar clusters were merged in the network 
biological replicates were set up for each developmental timeusing the mergeCloseModules function using a cutHeight value 
point. Total RNA was extracted with TRIzol reagent (Invitrogen,of 0.15. Module–trait associations were estimated using the cor- 
Carlsbad, CA, USA) following the manufacturer’s instructions.relation between the module eigengene and the phenotype (| 
RNA-seq libraries were constructed according to the manufac- PCC|  0.7, P-value  0.01), which allows easy identification of 
turer’s protocol of the Illumina NEBNext Ultra RNA Library Prepthe expression set (module) highly associated with the pheno- 
Kit (Illumina, Inc., San Diego, CA, USA). RNA sequencing with threetype. Hierarchical clustering was performed with the R package 
biological replications using an Illumina NovaSeq-PE150 Platform pheatmap (https://cran.r-project.org/web/packages/pheatmap/in- 
(Illumina, Inc.), which was completed by Novogene (Novogenedex.html) using PCC as the distance measure. Venn diagram sam- 
Co., Ltd., Tianjin, China). Sequencing reads were quality trimmedples were visualized with the R package UpSetR (https://cran.r- 
with Trimmomatic 0.38 [47]. After low-quality read removal, theproject.org/web/packages/UpSetR/index.html). The correlation 
remaining reads were aligned to the maize B73 reference genome relationship between samples was calculated with the R package 
(RefGen_v4;ftp://ftp.ensemblgenomes.org/pub/plants/release-Hmisc (https://cran.r-project.org/web/packages/Hmisc/index. 
41/fasta/zea_mays/dna) sequence assembly with HISAT2 2.0.5 html). 
[48]. StringTie 1.3.5 (https://ccb.jhu.edu/software/stringtie) was used to normalize and estimate gene expression levels in 
fragments per kilobase of transcript per million mapped reads3. Results (FPKM). The FPKM values of triplicate samples were averaged for 
each gene. Differentially expressed genes (DEGs) were identified 3.1. Phenotypic variation in KMC and KDR based on false discovery rate (FDR)-adjusted P-value  0.05 and 
a fold change  2 or  0.5 using edgeR [49]. Enrichment analysis We observed abundant variation in KMC and KDR in the AM212 
of Gene Ontology (GO) terms was performed with AgriGO 2.0panel. The inbred lines showed substantial variation in KMC, which 
(https://bioinfo.cau.edu.cn/agriGO/analysis.php) [50]. Transcrip-followed a near-normal distribution, with a range of values of 
tion factors (TFs) were identified by reference to GRASSIUS4.61%–31.66% at 10 developmental time points in the two years 
(https://grassius.org) [51] and PlantTFDB (https://planttfdb.cbi.(Fig. S1; Table S2). The KMC values were strongly correlated 
pku.edu.cn) [52].between the two years (Fig. S1A). The KMC data of 10 developmen- 
 tal time points were further transformed to KDR1 and KDR2 values 
2.6. Identification and quantitation of proteins using two methods (Fig. 1A). Analysis of variance suggested that 
 the variation of maize KMC, KDR1 and KDR2 was influenced mainly 
Maize kernels of maize inbred lines KA105 (FD3) and 91,227 by developmental stage, followed by genotype, environmental fac- 
(SD4) were sampled at 28, 35, 42, 49, and 56 DAP. Protein extrac-tors, and additional interaction effects (Fig. S1B). KMC, KDR1 and 
tion and peptide preparation were performed by Novogene (Novo- KDR2 showed high broad-sense heritability (H2), ranging from 
gene Co., Ltd.). Three biological replicates of the samples at each70.67% to 85.53% for KMC, 14.77% to 80.82% for KDR1, and 
time point were mixed as a pooled sample, and this pooled sample 79.03% to 89.79% for KDR2 (Fig. S1C). 
was used to construct the library for the data-independent acqui-We estimated the BLUP value of each inbred line across years 
sition (DIA) protein identification and the Mass Spectrum (MS) at each time point for KMC, KDR1, and KDR2. The BLUPs showed 
analysis for each sample as described in a previous study [53].normal distribution and were consistent with the variation in 
The data-dependent acquisition (DDA) MS raw files were ana-KMC, KDR1, and KDR2 at two years (Figs. 1B, S2). The range of 
lyzed with Proteome Discoverer 2.2, and peak lists were searched KMC variation in AM212 continuously decreased from the early 
against the SwissProt database (https://www.ebi.ac.uk/UniProt).to late stages, whereas the KDR at the early stage of kernel devel- 
MS1-based label-free quantification (LFQ) was performed usingopment was faster than that at the late stage (Fig. 1C). Cluster 
the maxLFQ algorithm [54]. MS2-based label-free quantification analysis revealed that AM212 KMC variation could be broadly 
was performed by analyzing DIA raw data using Biognosys Spec-divided into three types: inbred lines with slow dehydration (type 
tronaut 9.0. DIA MS/MS quantification is the sum of the integrated I), progressive dehydration (type II), and fast dehydration (type 
fragment ion peak areas. Subsequently, data were further analyzedIII) (Fig. S3). 
as described in a previous study with minor modifications [55]. At Additional phenotypic data were generated from the time ser- 
least one unique peptide with an FDR  1% was required for pro-ies phenotypic data (KMC, KDR1 and KDR2) for principal compo- 
tein identification and quantification. In the comparison group, a nent analysis (PCA)-based GWAS analysis, inspired by previous 
protein was assigned as a differently expressed protein (DEP) usingresearch [56]. For KMC, the first two principal components 
the cutoff criteria of an FDR-adjusted P-value  0.05 and a fold (PCs) explained respectively 63.32% and 12.32% of the total vari- 
change  1.5 or  0.67. To confirm quantitative protein, 20 pro- ance of development points, and the KMC at 42 DAP showed 
teins were randomly chosen and quantified by PRM analysis at high positive loadings on PC1 (78.08%) (Fig. 1D), suggesting that 
Novogene BioLabs (Novogene Co., Ltd.). 42 DAP may be a key time point for KMC transformation in late  kernel development. In contrast, the first 10 PCs of KDR1 
2.7. WGCNA (99.81%) and KDR2 (99.92%) explained nearly 100% of the KDR  variance among developmental stages (Figs. 1D, S4), and all 
 WGCNA was performed by the WGCNA R package (version PCs displayed roughly normal distributions (Fig. 1E). Accordingly, 
1.63;https://labs.genetics.ucla.edu/horvath/CoexpressionNet- these first 10 PCs of KMC, KDR1, and KDR2 were used as quan- 
work/Rpackages/WGCNA). The DEGs and DEPs identified across titative traits for GWAS.  249  


##### J. Qu, S. Xu, X. Gou et al.The Crop Journal 11 (2023) 247–257 
Fig. 1. Phenotypic diversity of 212 inbred lines. (A) Collection procedure of phenotype data. (B) Distribution of BLUP values for KMC and KDR. (C) Changes in BLUP values of 
KMC and KDR during kernel development. The change in KMC in individual inbred lines is depicted in gray lines, and colored lines indicate the overall pattern after fitting. (D) 
Loading plot of PC1 and PC2 based on BLUP values of KMC and KDR. Purple, green and yellow indicate clusters of developmental stages. The proportions of variance for PC1 
and PC2 are shown in parentheses. (E) Distribution of PC scores of KMC and KDR. KDR was calculated by two methods and named KDR1 and KDR2; see details in the Methods section. 
3.2. Genetic architecture of KMC and KDR(GEMMA) software for KMC and KDR, including all years and BLUP 
and PCA data (Fig. 2A–C). In total, 98 significantly associated loci 
 To characterize the genetic background of the association panel, (log10P  4.83) for KMC were detected with phenotypic variation 
we generated a final set of 67,076 high-quality single nucleotide explained (PVE) ranging from 0.22% to 22.92% (Fig. 2D–E), of which 
polymorphisms (SNPs) from the 6H90K Chip with a missing 20 loci were consistently detected at multiple time points, and 
rate < 0.20 and MAF > 0.05. PCA of these 67,076 SNPs showed thatapproximately 44% of KMC-associated loci (43/98) were located 
maize inbred lines from the Shaan A group and the Shaan B group in previously reported QTL intervals (Table S3). We detected 222 
were mostly well separated, and the 15 introduced inbred linesloci for KDR1 with 0.09% to 22.90% PVE and 107 loci for KDR2 with 
clustered with the Shaan B group (Fig. S5A). This observation was 0.71% to 23.51% PVE (Fig. 2D–E). Among these associated loci, 97 
also reflected by the phylogenetic relationships of the 212 inbredloci were repeatedly detected in multiple GWAS results, and 141 
lines, which were further divided into five main clades (Fig. S5B). loci were located in previously reported QTL intervals (Table S3). 
The LD decay distance was approximately 200 kb (r2 = 0.20)Specifically, 33 and 214 loci were uniquely detected for KMC and 
(Fig. S6), in agreement with a previous study using other maize KDR (Fig. 2D; Table S3), indicating that the variation in KMC and 
populations [57]. KDR was also associated with differences in their genetic basis. 
 To investigate the genetic basis of KMC and KDR, we performedOf 85 loci, 70 were detected using PCA-transformed phenotypic 
a GWAS using genome-wide efficient mixed-model associationdata instead of the BLUP values of KMC and KDR (Table S3). 250  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
Fig. 2. GWAS for KMC and KDR. (A–C) The colors of the dots correspond to a single trait, including all yearly and BLUP and PCA data. SNPs above red lines exceed a significance 
threshold (log10P  4.83). Only SNPs with  log10P  2 are plotted. Manhattan plot of GWAS associations for KMC (A), KDR1 (B) and KDR2 (C). (D) Colocalization of SNPs 
detected among KMC, KDR1 and KDR2. (E) Distribution of effect values of significant SNPs for KMC, KDR1, KDR2 and overall KDR. (F) Numbers of potential candidate genes for KMC and KDR traits. 
We further calculated the additive effects of significant loci for and a PCC > 0.7 with KMC was used for subsequent analysis 
KMC and KDR and found that these significant loci had 3.21%– (Fig. 3A). As a result, we identified 1406 and 608 genes that were 
42.70% additive effects for variance of KMC and 2.79%–42.82% unique to FD and SD, respectively, and 1097 genes overlapping 
additive effects for variance of KDR. The mean additive variance between FD and SD, including 92 TFs (Fig. 3B; Table S6). GO enrich- 
of significant loci for KDR was higher than that for KMC, far lowerment analysis showed that KMC-associated module genes detected 
than the broad-sense heritability (Fig. S7). These findings suggestspecifically for FD were enriched mainly in starch biosynthetic pro- 
that KMC and KDR are controlled by a few large-effect and many cess, stomatal movement, metal ion transport, and response to 
small-effect additive SNPs. We estimated a candidate region from light stimulus (Fig. 3C; Table S7). In contrast, KMC-associated mod- 
the flanking 200-kb regions of each significant SNP for KMC andule genes detected specifically for SD were significantly enriched in 
KDR. These regions contained 197 unique potential candidatebrassinosteroid homeostasis, lipid metabolic process, and cou- 
genes for KMC and 1363 unique potential candidate genes formarin biosynthetic process (Fig. 3C; Table S7). We identified genes 
KDR, with an overlap of 446 genes (Fig. 2F; Table S4). common to FD and SD that function in kernel development, includ- 
 ing seed dormancy process and organ senescence; steroid and alco- 
3.3. Identification of module genes and proteins highly associated withhol biosynthetic processes; chlorophyll catabolic process and lipid KMCstorage; nitrate and water transport; and multiple stress 
 responses, including freezing, heat acclimation, salt stress, desicca- 
To systematically investigate the relationship between gene/ tion, hydrogen peroxide, abscisic acid (ABA), and fructose 
protein activity and dynamic KMC, we performed high- responses (Fig. 3C; Table S7). 
throughput RNA-Seq and whole-proteome profiling for the kernels At the translation level, we applied both DIA and DDA work- 
of eight maize inbred lines with diverse dehydration types flows for whole-proteome profiling that quantified 6482 gene pro- 
(Figs. 3A, S8). At the transcription level, 26,393 genes wereductions with a 1% peptide FDR in at least two of three replicates 
expressed with a mean FPKM  1 of three biological replicates at per time point (Fig. 3A). A total of 3700 differentially expressed 
a minimum of one time point. After removing genes without signif-proteins (DEPs, P-value  0.05 and fold change  1.5 or  0.67) 
icant expression changes (FDR-adjusted P-value > 0.05 and/or were identified by pairwise comparisons, similar to those used in 
|log2(fold change)| < 1), we retained 17,435 genes with differential transcriptome comparison (Table S8). We performed PRM analysis 
expression between time points in the same inbred line for the on 20 proteins, revealing expression transitions similar to the DIA 
downstream weighted gene coexpression network analysis results (Fig. S9). 
(WGCNA) with the R package WGCNA [58] (Fig. 3A; Table S5).By comparing the proteins associated with KMC between FD and 
The KMC-associated modules were identified based on a Pear-SD, we found 559 (including 10 TFs) and 155 unique proteins (in- 
son correlation coefficient (PCC)  0.7 and a P-value  0.001. Tocluding 1 TF) for FD and SD, respectively, and 45 proteins 
further select promising genes for KMC, we considered only genes (including 1 TF) overlapping between FD and SD (Fig. 3D; 
that were uniformly detected in at least three FD or SD inbred lines,Table S9). GO enrichment analysis showed that unique proteins  251  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
Fig. 3. KMC-associated module genes and proteins and their functional diversity. (A) Workflow for identified module genes and proteins highly correlated with KMC. First, a 
coexpression network was constructed for each maize inbred line using temporal transcriptome and proteome data. Second, modules highly correlated with KMC were 
identified (PCC  0.70 and P-value  0.01). Third, module genes and proteins highly correlated with KMC were selected (|PCC|  0.70 and P-value  0.01). Finally, comparison 
of KMC-associated module genes and proteins in FD and SD. (B) Comparison of KMC-associated module genes in FD and SD. Red numbers in parentheses indicate TFs. (C) GO 
enrichment for KMC-associated module genes. (D) Comparison of KMC-associated module proteins in FD and SD. Red numbers in parentheses indicate TFs. (E) GO enrichment for KMC-associated module proteins. 
associated with FD play roles in kernel development, including pro- analysis,we identifiedfour genes(Zm00001d002258, 
line, short-chain fatty acid and starch biosynthetic processes; water Zm00001d002260, Zm00001d027290, and Zm00001d035920) that 
transport, callose deposition in the cell wall, cell wall pectin meta-were consistently linked to KMC and KDR at the multiomics level 
bolic process, NADPH regeneration, the tricarboxylic acid cycle and (Fig. 4A). Zm00001d035920, encoding an RNA binding protein, is a 
gluconeogenesis; and response to heat, desiccation, hydrogen per- binding partner of ACD11.1, hereafter named ZmBPACD11. Within 
oxide and cytokinin (Fig. 3D; Table S10). In contrast, unique pro-this gene, two adjacent SNPs (Affx-291435855 and Affx- 
teins for SD were linked to lipid localization, killing of cells of 291445022) were significantly associated with KMC and KDR 
other organisms and response to hypoxia and oxidative stress(Fig. 4B–C). ZmBPACD11 showed lower gene expression levels but 
(Fig. 3D; Table S10). Overlapping proteins were associated with cel-higher protein abundance in FD than in SD inbred lines (Fig. 4D). 
lular amine and sulfur compound metabolic processes and hor-Protein–protein interaction analysis showed that ZmBPACD11 
mone and pigment biosynthetic processes (Fig. 3D; Table S10). (B4FEG8) has potential interactions with six proteins, of which A0A1D6DZ56 encodes an ABC transporter and has been verified 
3.4. Identification and validation of candidate genes associated with to be involved in diverse processes, such as pathogen response, 
KMC and KDR surface lipid deposition, phytate accumulation in seeds, and trans- 
port of the phytohormones auxin and ABA (Fig. 4E) [59]. This result 
 Integrating GWAS analysis, network-based temporal transcrip- suggests that ZmBPACD11 is likely to be a key candidate gene for 
tome data analysis and network-based temporal proteome data KMC and KDR. 252  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
Fig. 4. ZmBPACD11 is a potential candidate gene for KMC and KDR. (A) UpSet plot showing the number of genes associated to KMC and KDR that were detected by multiomics. 
(B) The upper panel indicates GWAS of the BLUP value for KMC at 56 DAP and KDR2 from 49 DAP to 56 DAP. The lower panel indicates the P values of SNPs surrounding a 1- 
Mb region upstream and downstream of the lead SNP on chromosome 6, gene model of ZmBPACD11 and LD pattern of the ZmBPACD11 region. The red stars mark the positions 
of the lead SNP. (C) The influence of the lead SNPs on KMC and KDR. The significance of the difference between two genotypes was evaluated by two-tailed Student’s t-test. 
(D) Expression patterns of ZmBPACD11 at the transcriptional and translational levels. (E) Protein interaction network of ZmBPACD11.  253  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
Another GWAS locus on chromosome 9 was associated with and responding to multiple stresses, including seed dormancy pro- 
KDR at multiple kernel developmental stages. In the candidatecess and response to ABA, hydrogen peroxide, desiccation, salt 
region, there was one candidate gene Zm00001d047799, transcrip-stress, cold, heat acclimation, and high light intensity (Fig. S10; 
tional and translational changes of which were significantly Table S11). These results indicate that the ZmHSP5 function affects 
associated with changes in KMC (Fig. 5A–C; Tables S6, S9). KMC and, in turn, KDR. Zm00001d047799 encodes heat shock 70 kDa protein 5, which has been reported to function in protein folding, calcium home- 
ostasis, and serves as an essential regulator of the endoplasmic 4. Discussion 
reticulum (ER) stress response and autophagy [60,61] and is here- 
after named ZmHSP5. This gene showed a higher gene expressionIn this study, multiple highly promising candidate genes associ- 
level and lower protein abundance at the late stage of kernelated with KMC and KDR were identified, and these genes may drive 
development in FD than in SD (Fig. 5D). To further determine the multiple metabolic processes in maize kernel development. This 
potential function of ZmHSP5, we identified an EMS mutantlarge collection of genes provides a rich resource for investigating 
(EMS4-0be358) carrying a C-to-T substitution in the second exonthe genetic basis of KMC and KDR throughout maize seed develop- 
that results in CAG becoming the stop codon TAG, thus introducingment, cloning KMC- and KDR-associated genes, and designing pre- 
a premature stop codon (Fig. 5E). KMC was significantly lower in cision breeding strategies. These data also provide many missing 
homozygous HSP5 plants than in their homozygous wild-type sib- details for studying the spatiotemporal regulation of development 
lings, and KDR was also faster in homozygous HSP5 plants than in processes in maize kernels. 
their homozygous wild-type siblings at the late stage of kernelKMC and KDR are both complex quantitative traits regulated by 
development (Fig. 5F). WGCNA showed that 120 genes were con- multiple genetic factors and perturbed by a variety of environmen- 
sistently detected in the coexpression networks of at least twotal factors, including humidity, temperature, radiation, wind speed, 
maize inbred lines and synchronized with ZmHSP5 expression,and rainfall [4]. Thus, obtaining an accurate phenotype is a prereq- 
and they were enriched mainly in regulating kernel development uisite for KMC- and KDR-associated research. To eliminate the 
Fig. 5. ZmHSP5 affected KDR. (A) Manhattan plot of the GWAS for KDR2 from 14 DAP to 56 DAP in 2019. The lead SNP is indicated by a red dot. (B) The upper panel shows the 
P values of SNPs surrounding a 1-Mb region upstream and downstream of the lead SNP. The middle panel shows the gene model of ZmHSP5 (v3). The lower panel shows LD 
pattern of the ZmHSP5 region. Red stars mark the positions of the lead SNP. (C) The effect of the genotype on KDR2 in the association-mapping population. (D) Expression 
patterns of ZmHSP5 at the transcriptional and translational levels. (E) Genotype of the wild type (WT) and HSP5 and the position of mutation on ZmHSP5 (v4). The blue shading 
indicates the mutated nucleotide. In (C) and (E), the significance of the difference between two genotypes was evaluated by two-tailed Student’s t-test. (F) Quantification of KMC and KDR between the WT and HSP5 from 35 DAP to 49 DAP.  254  


##### J. Qu, S. Xu, X. Gou et al. The Crop Journal 11 (2023) 247–257 
influence of environmental factors, the following measures werealready gained their germination capacity and desiccation toler- 
taken in this study: (1) inbred lines with similar growth periodsance. Some biological processes have been found [73,80,81] to 
were selected, (2) pollination dates were adjusted according tofunction in seed development and influence seed dehydration, 
the flowering time of materials and centralized pollination, and including the accumulation of disaccharides, oligosaccharides, 
(3) uniform samples were collected with the same pollination date. and the plant hormone ABA; synthesis of storage proteins, late 
In addition, the selection of the measurement method is crucial forembryogenesis-abundant proteins and heat-shock proteins; acti- 
obtaining accurate KMC values, and many methods have beenvation of antioxidative defenses; changes in the physical structure 
reported for measuring KMC, including the SK300 moisture-of the cell; and a gradual and steady increase in density. In this 
determination meter [62], the digital timber-moisture meter andstudy, gene sets associated with KMC and KDR were enriched in 
the electrophysics moisture meter model MT808 [28,31,36].a variety of unreported biological processes, including the biosyn- 
Although these methods are effective, it is necessary to considerthesis process of fatty acids, glucan, starch and jasmonic acid; cell 
the effective range of measurement, the position at which thecycle; and glycolytic process, and they were also linked to various 
probe penetrates the kernel, and whether precise calibration iskernel desiccation tolerance processes, including response to water 
required. We chose an improved oven-drying method with rela- deprivation, heat, hydrogen peroxide, reactive oxygen species, 
tively high accuracy to measure KMC, although it is time-fatty acid beta-oxidation and oxidation–reduction processes 
consuming and labor-intensive [19,32,63].(Tables S6, S9). The content of amylopectin with a degree of poly- 
In addition to the determined phenotype data, PCA is also an merization of 6–12 was lower in inbred lines with fast KDR [82]. 
effective evaluation means for complex quantitative traits. PCA is These results provide a new perspective for understanding the bio- 
valuable for extracting underlying factors for multiple traits bylogical processes that affect maize KMC and KDR. We provide 
reducing dimensionality, and PC scores as dependent variablesdetailed transcriptional and translational information on the spa- 
are proposed as a strategy for performing efficient GWAS [56,64– tiotemporal patterns of all these genes associated with KMC and 
66]. PC scores produced by PCA can transform skewed original KDR. Although the underlying molecular mechanism of these gene 
variables into approximate normal distributions, resulting insets associated with KMC and KDR should be further investigated, 
robust, reliable GWAS results [67,68]; GWAS using PC scores maymultiple GWAS data combining spatiotemporal transcriptome and 
detect genomic regions that could be overlooked by use of individ- proteomic data provide genetic resources for mining key genes for 
ual traits, given that PC scores represent integrated variables. InKMC and KDR. this study, we performed a GWAS and identified 98 and 279 loci 
associated with KMC and KDR, respectively (Table S3). Of these Declaration of competing interest 
loci, a GWAS of 10 PCA datasets detected 15 loci consistent with 
the results of the GWAS for the yearly and BLUP datasets and iden- The authors declare that they have no known competing finan- 
tified 70 loci controlled by genetic factors that were detectedcial interests or personal relationships that could have appeared to 
specifically from PCA-transformed phenotypic data. influence the work reported in this paper. Most loci had small effects on KMC and KDR variation, suggest- 
ing that the sum of many SNPs with small effects is responsible for  CRediT authorship contribution statement 
the main contribution to the genetic basis of the variations in KMC 
and KDR. In comparison with previous studies [16,19,27,62,69–72],  Jianzhou Qu: Investigation, Data curation, Methodology, Soft- 
approximately half of the loci were located in reported QTL inter- 
 ware, Visualization, Writing – Original draft. Shutu Xu: Conceptu- 
vals (Table S3). This finding could be the result of differences in 
 alization, Supervision, Validation, Writing – review & editing. genetic backgrounds, population size, captured recombinant 
 Xiaonan Gou: Investigation, Validation. Hao Zhang: Investigation, events, environmental effects, and GWAS analytical methods.  Validation. Qian Cheng: Software, Validation. Xiaoyue Wang: These loci identified during dynamic kernel development consti- 
 Investigation, Validation. Chuang Ma: Conceptualization, Supervi- 
tute a resource that can be used for accelerating mining of superior 
 sion, Visualization, Validation, Writing – review & editing. Jiquan alleles for KMC and KDR. 
 Xue: Conceptualization, Supervision, Validation, Writing – review Seed dehydration from the phase of reserve accumulation to  & editing. 
maturation drying is associated with distinct gene/protein expres- 
sion and metabolic switches [73]. One critical question is which 
specific genes function in regulatory metabolic pathways and the Data availability gene regulatory network associated with maize KMC and KDR. 
Previous genetic studies have demonstrated the functional signifi-All phenotype data of inbred maize lines in this study are 
cance of certain genes in seed maturation and dehydration. Over- included in Table S1. All RNA-seq data generated in this study have 
expressing the LEA Rab28 gene increased the water-stress been submitted to the NCBI Gene Expression Omnibus (GEO; 
tolerance of transgenic maize plants [74,75], and abi3 and vp1 https://www.ncbi.nlm.nih.gov/geo) under accession number 
mutations increased the desiccation tolerance of seeds [76,77].GSE158816. The MS raw data generated in this study have been 
ATEM6 mutation and overexpression of AtMYB118 caused prema-submitted to ProteomeXchange database (www.proteomex- 
ture dehydration of seeds [78,79], and GAR2 affected maize KDR change.org) via the iProX partner repository under accession num- 
[28]. However, such well-studied genes represent a small propor- ber PXD021680. All other reasonable requests for data and 
tion of the genes associated with KMC and KDR that we have research materials should be addressed to the corresponding 
detected. We integrated GWAS, transcriptomics, and proteomicsauthors. data and identified additional highly promising genes, such as 
ZmBPACD11 and ZmHSP5. This was especially true for ZmHSP5, Acknowledgments which was confirmed by mutation. 
The water loss of maize kernels is associated not only with the This research was supported by Natural Science Foundation of 
accumulation of storage material processes before physiologicalShaanxi Province (S2021-JC-WT-006), the National Key Research 
maturity. As water concentration declines, damaging processesand Development Program of China (2018YFD0100200), the China 
can occur, and seeds must have, or acquire, mechanisms to protectPostdoctoral Science Foundation (2018M633588) and the China 
against them. Seeds entering the late maturation phase haveAgriculture Research System (CARS-02-77). We thank all members  255  


##### J. Qu, S. Xu, X. Gou et al.The Crop Journal 11 (2023) 247–257 
in the Key Laboratory of Biology and Genetic Improvement of [28] W. Li, Y. Yu, L. Wang, Y. Luo, Y. Peng, Y. Xu, X. Liu, S. Wu, L. Jian, J. Xu, Y. Xiao, J. 
 Yan, The genetic architecture of the dynamic changes in grain moisture in Maize in Arid Area of Northwest Region for their helps and sup-  maize, Plant Biotechnol. J. 19 (2021) 1195–1205. 
ports in field material planting and phenotype collection.[29] J. Yu, E.S. Buckler, Genetic association mapping and genome organization of  maize, Curr. Opin. Biotechnol. 17 (2006) 155–160. 
[30] J. Yan, M. Warburton, J. Crouch, Association mapping for enhancing maize (Zea 
Appendix A. Supplementary data mays L.) genetic improvement, Crop Sci. 51 (2011) 433–449. 
[31] G. Zhou, D. Hao, L. Xue, G. Chen, H. Lu, Z. Zhang, M. Shi, XiaoLan Huang, Y. Mao, 
 Genome-wide association study of kernel moisture content at harvest stage in 
 Supplementary data for this article can be found online atmaize, Breed. Sci. 68 (2018) 622–628. 
https://doi.org/10.1016/j.cj.2022.04.017. [32] T. Jia, L. Wang, J. Li, J. Ma, Y. Cao, T. Lubberstedt, H. Li, Integrating a genome- 
 wide association study with transcriptomic analysis to detect genes 
 controlling grain drying rate in maize (Zea mays L.), Theor. Appl. Genet. 133 References (2020) 623–634. 
[33] L. Dai, L. Wu, Q. Dong, Z. Zhang, N. Wu, Y. Song, S. Lu, P. Wang, Genome-wide 
 association study of field grain drying rate after physiological maturity based on 
 [1] R.G. Sala, F.H. Andrade, J.C. Cerono, Quantitative trait loci associated with grain 
 a resequencing approach in elite maize germplasm, Euphytica 213 (2017) 182. 
 moisture at harvest for line per se and testcross performance in maize: a meta- 
[34] T. Li, J.Z. Qu, X.K. Tian, Y.H. Lao, N.N. Wei, Y.H. Wang, Y.C. Hao, X.H. Zhang, J.Q.  analysis, Euphytica 185 (2012) 429–440. 
 Xue, S.T. Xu, Identification of ear morphology genes in maize (Zea mays L.) 
 [2] L.L. Li, X.P. Lei, R.Z. Xie, K.R. Wang, P. Hou, F.L. Zhang, S.K. Li, Analysis of 
 using selective sweeps and association mapping, Front. Genet. 11 (2020) 747. 
 influential factors on mechanical grain heavest quality of summer maize, Sci. 
[35] X. Lu, J. Liu, W. Ren, Q. Yang, Z. Chai, R. Chen, L. Wang, J. Zhao, Z. Lang, H. Wang, 
 Agric. Sin. 50 (2017) 2044–2051 (in Chinese with English abstract). 
 Y. Fan, J. Zhao, C. Zhang, Gene-indexed mutations In maize, Mol. Plant 11 
 [3] K. Xiang, L.M. Reid, Z.M. Zhang, X.Y. Zhu, G.T. Pan, Characterization of  (2018) 496–504. 
 correlation between grain moisture and ear rot resistance in maize by QTL 
[36] J. Yang, M.J. Carena, J. Uphaus, Area Under the Dry Down Curve (AUDDC): a  meta-analysis, Euphytica 183 (2012) 185–195. 
 method to evaluate rate of dry down in maize, Crop Sci. 50 (2010) 2347–2354. 
 [4] I.R. Brooking, Maize ear moisture during grain-filling, and its relation to 
[37] S.J. Knapp, W.W. Stroup, W.M. Ross, Confidence intervals for heritability for 
 physiological maturity and grain-drying, Field Crops Res. 23 (1990) 55–68. 
 two-factor mating design single environment linear models, Crop Sci. 25 
 [5] J.L. Schmidt, A.R. Hallauer, Estimating harvest date of corn in the field, Crop Sci.  (1985) 192.  6 (1966) 227–231. 
[38] M.G. Murray, W.F. Thompson, Rapid isolation of high molecular weight plant 
 [6] H.Z. Cross, J.R. Chyle Jr., J.J. Hammond, Divergent selecting for ear moisture in  DNA, Nucleic Acids Res. 8 (1980) 4321–4326.  early maize, Crop Sci. 27 (1987) 914–918. 
[39] S. Purcell, B. Neale, K. Todd-Brown, L. Thomas, M.A. Ferreira, D. Bender, J. 
 [7] M.T. Hillson, L.H. Penny, Dry matter accumulation and moisture loss during 
 Maller, P. Sklar, P.I. de Bakker, M.J. Daly, P.C. Sham, PLINK: a tool set for whole-  maturation of corn grain, Agron. J. 57 (1965) 150–153. 
 genome association and population-based linkage analyses, Am. J. Hum. 
 [8] H.G. Nass, P.L. Crane, Effect of endosperm mutants on drying rate in corn (Zea  Genet. 81 (2007) 559–575.  mays L.), Crop Sci. 10 (1970) 141–144. 
[40] B.L. Browning, Y. Zhou, S.R. Browning, A one-penny imputed genome from 
 [9] D. Mišević, D.E. Alexander, J. Dumanović, B. Kerečki, S. Ratković, Grain moisture 
 next-generation reference panels, Am. J. Hum. Genet. 103 (2018) 338–348. 
 loss rate of high-oil and standard-oil maize hybrids, Agron. J. 80 (1988) 841– 
[41] X. Zhou, M. Stephens, Genome-wide efficient mixed-model analysis for  845.  association studies, Nat. Genet. 44 (2012) 821–824. 
[10] P.L. Crane, S.R. Miles, J.E. Newman, Factors associated with varietal differences 
[42] S. Lê, J. Josse, F. Husson, FactoMineR: an R package for multivariate analysis, J.  in rate of field drying in corn, Agron. J. 51 (1959) 318–320.  Stat. Softw. 25 (2008) 1–18. 
[11] J.L. Purdy, P.L. Crane, Influence of pericarp on differential drying rate in 
[43] J. Yang, S.H. Lee, M.E. Goddard, P.M. Visscher, GCTA: a tool for genome-wide  ‘‘mature” corn (Zea mays L.), Crop Sci. 7 (1967) 379–381.  complex trait analysis, Am. J. Hum. Genet. 88 (2011) 76–82. 
[12] A.J. Cavalieri, O.S. Smith, Grain filling and field drying of a set of maize hybrids 
[44] S. Kumar, G. Stecher, M. Li, C. Knyaz, K. Tamura, MEGA X: molecular  released from to 1982, Crop Sci. 25 (1930) 856–860. 
 evolutionary genetics analysis across computing platforms, Mol. Biol. Evol. 
[13] D.R. Hicks, G.L. Geadelmann, R.H. Peterson, Drying rates of frosted maturing  35 (2018) 1547–1549.  maize, Agron. J. 68 (1976) 452–455. 
[45] J. Yang, T.A. Manolio, L.R. Pasquale, E. Boerwinkle, N. Caporaso, J.M. 
[14] P.M. Sweeney, S.K. St. Martin, C.P. Clucas, Indirect inbred selection to reduce 
 Cunningham, M. de Andrade, B. Feenstra, E. Feingold, M.G. Hayes, W.G. Hill,  grain moisture in maize hybrids, Crop Sci. 34 (1994) 391–396. 
 M.T. Landi, A. Alonso, G. Lettre, P. Lin, H. Ling, W. Lowe, R.A. Mathias, M. 
[15] A.F. Troyer, W.B. Ambrose, Plant characteristics affecting field drying rate of 
 Melbye, E. Pugh, M.C. Cornelis, B.S. Weir, M.E. Goddard, P.M. Visscher, Genome  ear corn, Crop Sci. 11 (1971) 529–531. 
 partitioning of genetic variation for complex traits using common SNPs, Nat. 
[16] D.F. Austin, M. Lee, L.R. Veldboom, A.R. Hallauer, Genetic mapping in maize  Genet. 43 (2011) 519–525. 
 with hybrid progeny across testers and generations: grain yield and grain 
[46] M.X. Li, J.M.Y. Yeung, S.S. Cherny, P.C. Sham, Evaluating the effective numbers  moisture, Crop Sci. 40 (2000) 30–39. 
 of independent tests and significant p-value thresholds in commercial 
[17] R.G. Sala, F.H. Andrade, E.L. Camadro, J.C. Cerono, Quantitative trait loci for 
 genotyping arrays and public imputation reference datasets, Hum. Genet. 
 grain moisture at harvest and field grain drying rate in maize (Zea mays L.),  131 (2012) 747–756.  Theor. Appl. Genet. 112 (2006) 462–471. 
[47] A.M. Bolger, M. Lohse, B. Usadel, Trimmomatic: a flexible trimmer for Illumina 
[18] W. Song, Z.I. Shi, J. Xing, M. Duan, A. Su, C. Li, R. Zhang, Y. Zhao, M. Luo, J. Wang,  sequence data, Bioinformatics 30 (2014) 2114–2120. 
 J. Zhao, T. Lübberstedt, Molecular mapping of quantitative trait loci for grain 
[48] D. Kim, B. Langmead, S.L. Salzberg, HISAT: a fast spliced aligner with low  moisture at harvest in maize, Plant Breed. 136 (2017) 28–32.  memory requirements, Nat. Methods 12 (2015) 357–360. 
[19] J. Liu, H. Yu, Y. Liu, S. Deng, Q. Liu, B. Liu, M. Xu, Genetic dissection of grain 
[49] M.D. Robinson, D.J. McCarthy, G.K. Smyth, edgeR: a Bioconductor package for 
 water content and dehydration rate related to mechanical harvest in maize, 
 differential expression analysis of digital gene expression data, Bioinformatics  BMC Plant Biol. 20 (2020) 118.  26 (2010) 139–140. 
[20] W.D. Beavis, O.S. Smith, D. Grant, R. Fincher, Identification of quantitative trait 
[50] Z. Du, X. Zhou, Y. Ling, Z. Zhang, Z. Su, agriGO: a GO analysis toolkit for the 
 loci using a small sample of topcrossed and F4 progeny from maize, Crop Sci.  agricultural community, Nucleic Acids Res. 38 (2010) 64–70.  34 (1994) 882–896. 
[51] A. Yilmaz, M.Y. Nishiyama Jr., B.G. Fuentes, G.M. Souza, D. Janies, J. Gray, E. 
[21] J. Zhang, F. Zhang, B. Tang, Y. Ding, L. Xia, J. Qi, X. Mu, L. Gu, D. Lu, Y. Chen, 
 Grotewold, GRASSIUS: a platform for comparative regulatory genomics across 
 Molecular mapping of quantitative trait loci for grain moisture at harvest and  the grasses, Plant Physiol. 149 (2009) 171–180. 
 field grain drying rate in maize (Zea mays L.), Physiol. Plant. 169 (2019) 64–72. 
[52] J. Jin, F. Tian, D.C. Yang, Y.Q. Meng, L. Kong, J. Luo, G. Gao, PlantTFDB 4.0: 
[22] G. Blanc, A. Charcosset, B. Mangin, A. Gallais, L. Moreau, Connected populations 
 toward a central hub for transcription factors and regulatory interactions in 
 for detecting quantitative trait loci and testing for epistasis: an application in  plants, Nucleic Acids Res. 45 (2017) 1040–1045.  maize, Theor. Appl. Genet. 113 (2006) 206–224. 
[53] B.O. Jia, X. Zhao, D.I. Wu, Z. Dong, Y. Chi, J. Zhao, M. Wu, T. An, Y. Wang, M. 
[23] J. Ho, S. McCouch, M. Smith, Improvement of hybrid yield by advanced 
 Zhuo, J. Li, X. Chen, G. Tian, J. Long, X. Yang, H. Chen, J. Wang, X. Zhai, S. Li, J. Li, 
 backcross QTL analysis in elite maize, Theor. Appl. Genet. 105 (2002) 440–448. 
 M. Ma, Y. He, L. Kong, L. Brcic, J. Fang, Z. Wang, Identification of serum 
[24] E. Frascaroli, M.A. Cane, P. Landi, G. Pea, L. Gianfranceschi, M. Villa, M. 
 biomarkers to predict pemetrexed/platinum chemotherapy efficacy for 
 Morgante, M.E. Pe, Classical genetic and quantitative trait loci analyses of 
 advanced lung adenocarcinoma patients by data-independent acquisition 
 heterosis in a maize hybrid between two elite inbred lines, Genetics 176 
 (DIA) mass spectrometry analysis with parallel reaction monitoring (PRM)  (2007) 625–644.  verification, Tranl. Lung Cancer Res. 10 (2021) 981–994. 
[25] A.E. Melchinger, H.F. Utz, C.C. Schön, Quantitative trait locus (QTL) mapping 
[54] J. Cox, M.Y. Hein, C.A. Luber, I. Paron, N. Nagaraj, M. Mann, Accurate proteome- 
 using different testers and independent population samples in maize reveals 
 wide label-free quantification by delayed normalization and maximal peptide 
 low power of QTL detection and large bias in estimates of QTL effects, Genetics 
 ratio extraction, termed MaxLFQ, Mol. Cell Proteomics 13 (2014) 2513–2526.  149 (1998) 383–403. 
[55] R. Bruderer, O.M. Bernhardt, T. Gandhi, S.M. Miladinović, L.Y. Cheng, S. 
[26] R. Mihaljevic, C.C. Schön, H.F. Utz, A.E. Melchinger, Correlations and QTL 
 Messner, T. Ehrenberger, V. Zanotelli, Y. Butscheid, C. Escher, O. Vitek, O. 
 correspondence between line per se and testcross performance for agronomic 
 Rinner, L. Reiter, Extending the limits of quantitative proteome profiling with 
 traits in four populations of european maize, Crop Sci. 45 (2005) 114–122. 
 data-independent acquisition and application to acetaminophen-treated 
[27] Z. Wang, X. Wang, L. Zhang, X. Liu, H. Di, T. Li, X. Jin, QTL underlying field grain 
 three-dimensional liver microtissues, Mol. Cell Proteomics 14 (2015) 1400– 
 drying rate after physiological maturity in maize (Zea mays L.), Euphytica 185  1410.  (2012) 521–528. 256  


##### J. Qu, S. Xu, X. Gou et al.The Crop Journal 11 (2023) 247–257 
[56] C. Miao, Y. Xu, S. Liu, P.S. Schnable, J.C. Schnable, Increased power and accuracycandidate genes for desiccation and abscisic acid content in maize kernels, 
 of causal locus identification in time series genome-wide association inBMC Plant Biol. 10 (2010) 2. 
 sorghum, Plant Physiol. 183 (2020) 1898–1909.[70] L.A. Robertson-Hoyt, C.E. Kleinschmidt, D.G. White, G.A. Payne, C.M. Maragos, 
[57] M. Wang, J. Yan, J. Zhao, W. Song, X. Zhang, Y. Xiao, Y. Zheng, Genome-wide J.B. Holland, Relationships of resistance to fusarium ear rot and fumonisin 
 association study (GWAS) of resistance to head smut in maize, Plant Sci. 196contamination with agronomic performance of maize, Crop Sci. 47 (2007)  (2012) 125–131. 1770–1778. 
[58] P. Langfelder, S. Horvath, WGCNA: an R package for weighted correlation[71] X.J. Liu, Z.H. Wang, X. Wang, T.F. Li, L. Zhang, Primary mapping of QTL for 
 network analysis, BMC Bioinform. 9 (2008) 559.dehydration rate of maize kernel after physiological maturing, Acta Agron. Sin. 
[59] J. Kang, J. Park, H. Choi, B. Burla, T. Kretzschmar, Y. Lee, E. Martinoia, Plant ABC36 (2010) 47–52 (in Chinese with English abstract). 
 transporters, Arabidopsis Book 9 (2011) e0153. [72] Y.L. Li, Y.B. Dong, M.L. Yang, Q.L. Wang, Q.L. Shi, Q. Zhou, F. Deng, Z.Y. Ma, D.H. 
[60] K.L. Cook, A.N. Shajahan, A. Wärri, L.u. Jin, L.A. Hilakivi-Clarke, R. Clarke,Qiao, H. Xu, QTL Detection for grain water relations and genetic correlations 
 Glucose-regulated protein 78 controls cross-talk between apoptosis andwith grain matter accumulation at four stages after pollination in maize, J. 
 autophagy to determine antiestrogen responsiveness, Cancer Res. 72 (2012) Physiol. Biochem. 2 (2014) 1. 
 3337–3349. [73] R. Angelovici, G. Galili, A.R. Fernie, A. Fait, Seed desiccation: a bridge between 
[61] W. Shi, G. Xu, C. Wang, S.M. Sperber, Y. Chen, Q. Zhou, Y.I. Deng, H. Zhao, Heatmaturation and germination, Trends Plant Sci. 15 (2010) 211–218. 
 shock 70-kDa protein 5 (Hspa5) is essential for pronephros formation by[74] I. Amara, M. Capellades, M.D. Ludevid, M. Pagès, A. Goday, Enhanced water 
 mediating retinoic acid signaling, J. Biol. Chem. 290 (2015) 577–589. stress tolerance of transgenic maize plants over-expressing LEA Rab28 gene, J. 
[62] Y.L. Qian, X.Q. Zhang, L.F. Wang, J. Chen, B.R. Chen, G.H. Lv, Z.C. Wu, J. Guo, J.Plant Physiol. 170 (2013) 864–873. 
 Wang, Y.C. Qi, T.C. Li, W. Zhang, L. Ruan, X.L. Zuo, Detection of QTLs controlling [75] M. Pla, J. Gómez, A. Goday, M. Pagès, Regulation of the abscisic acid-responsive 
 fast kernel dehydration in maize (Zea mays L.), Genet. Mol. Res. 15 (2016), gene rab28 in maize viviparous mutants, Mol. Gen. Genet. 230 (1991) 394–  gmr.15038151. 400. 
[63] R.G. Sala, F.H. Andrade, M.E. Westgate, Maize kernel moisture at physiological [76] D.R. McCarty, Genetic control and integration of maturation and germination 
 maturity as affected by the source-sink relationship during grain filling, Crop pathways in seed development, Annu. Rev. Plant Biol. 46 (1995) 71–93. 
 Sci. 47 (2007) 711–714.[77] F. Parcy, C. Valon, A. Kohara, S. Miséra, J. Giraudat, The ABSCISIC ACID- 
[64] L.N. He, Y.J. Liu, P. Xiao, L. Zhang, Y. Guo, T.L. Yang, L.J. Zhao, B. Drees, J.INSENSITIVE3, FUSCA3, and LEAFY COTYLEDON1 loci act in concert to control 
 Hamilton, H.Y. Deng, R.R. Recker, H.W. Deng, Genomewide linkage scan formultiple aspects of Arabidopsis seed development, Plant Cell 9 (1997) 1265– 
 combined obesity phenotypes using principal component analysis, Ann. Hum. 1277. 
 Genet. 72 (2008) 319–326.[78] A.J. Manfre, G.A. LaHatte, C.R. Climer, W.R. Marcotte Jr., Seed dehydration and 
[65] C.J. Holberg, M. Halonen, S. Solomon, P.E. Graves, M. Baldini, R.P. Erickson, F.D.the establishment of desiccation tolerance during seed maturation is altered in 
 Martinez, Factor analysis of asthma and atopy traits shows 2 majorthe Arabidopsis thaliana mutant atem6-1, Plant Cell Physiol. 50 (2009) 243– 
 components, one of which is linked to markers on chromosome 5q, J. Allergy253. 
 Clin. Immunol. 108 (2001) 772–780. [79] Y. Zhang, G. Cao, L.J. Qu, H. Gu, Involvement of an R2R3-MYB transcription 
[66] K. Yano, Y. Morinaka, F. Wang, P. Huang, S. Takehara, T. Hirai, A. Ito, E. Koketsu, factor gene AtMYB118 in embryogenesis in Arabidopsis, Plant Cell Rep. 28 
 M. Kawamura, K. Kotake, S. Yoshida, M. Endo, G. Tamiya, H. Kitano, M. (2009) 337–346. 
 Ueguchi-Tanaka, K.O. Hirano, M. Matsuoka, GWAS with principal component[80] O. Leprince, A. Pellizzaro, S. Berriri, J. Buitink, Late seed maturation: drying 
 analysis identifies a gene comprehensively controlling rice architecture, Proc. without dying, J. Exp. Bot. 68 (2017) 827–841. 
 Natl. Acad. Sci. U. S. A. 116 (2019) 21262–21267.[81] K. Righetti, J.L. Vu, S. Pelletier, B.L. Vu, E. Glaab, D. Lalanne, A. Pasha, R.V. Patel, 
[67] D.I. Boomsma, C.V. Dolan, A comparison of power to detect a QTL in sib-pair N.J. Provart, J. Verdier, O. Leprince, J. Buitink, Inference of longevity-related 
 data using multivariate phenotypes, mean phenotypes, and factor scores, genes from a robust coexpression network of seed maturation identifies 
 Behav. Genet. 28 (1998) 329–340.regulators linking seed storability to biotic defense-related pathways, Plant 
[68] L. Goh, V.B. Yap, Effects of normalization on quantitative traits in associationCell 27 (2015) 2692–2708. 
 test, BMC Bioinformatics 10 (2009) 415.[82] J. Qu, Y. Zhong, L. Ding, X. Liu, S. Xu, D. Guo, A. Blennow, J. Xue, Biosynthesis, 
[69] V. Capelle, C. Remoue, L. Moreau, A. Reyss, A. Mahe, A. Massonneau, M. Falque,structure and functionality of starch granules in maize inbred lines with 
 A. Charcosset, C. Thevenot, P. Rogowsky, S. Coursol, J.L. Prioul, QTLs anddifferent kernel dehydration rate, Food Chem. 368 (2022) 130796. 257  