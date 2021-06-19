# TF::Aiven::Elasticsearch ElasticsearchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionautocreateindexenabled" title="ActionAutoCreateIndexEnabled">ActionAutoCreateIndexEnabled</a>" : <i>String</i>,
    "<a href="#actiondestructiverequiresname" title="ActionDestructiveRequiresName">ActionDestructiveRequiresName</a>" : <i>String</i>,
    "<a href="#clustermaxshardspernode" title="ClusterMaxShardsPerNode">ClusterMaxShardsPerNode</a>" : <i>String</i>,
    "<a href="#httpmaxcontentlength" title="HttpMaxContentLength">HttpMaxContentLength</a>" : <i>String</i>,
    "<a href="#httpmaxheadersize" title="HttpMaxHeaderSize">HttpMaxHeaderSize</a>" : <i>String</i>,
    "<a href="#httpmaxinitiallinelength" title="HttpMaxInitialLineLength">HttpMaxInitialLineLength</a>" : <i>String</i>,
    "<a href="#indicesfielddatacachesize" title="IndicesFielddataCacheSize">IndicesFielddataCacheSize</a>" : <i>String</i>,
    "<a href="#indicesmemoryindexbuffersize" title="IndicesMemoryIndexBufferSize">IndicesMemoryIndexBufferSize</a>" : <i>String</i>,
    "<a href="#indicesqueriescachesize" title="IndicesQueriesCacheSize">IndicesQueriesCacheSize</a>" : <i>String</i>,
    "<a href="#indicesqueryboolmaxclausecount" title="IndicesQueryBoolMaxClauseCount">IndicesQueryBoolMaxClauseCount</a>" : <i>String</i>,
    "<a href="#reindexremotewhitelist" title="ReindexRemoteWhitelist">ReindexRemoteWhitelist</a>" : <i>[ String, ... ]</i>,
    "<a href="#searchmaxbuckets" title="SearchMaxBuckets">SearchMaxBuckets</a>" : <i>String</i>,
    "<a href="#threadpoolanalyzequeuesize" title="ThreadPoolAnalyzeQueueSize">ThreadPoolAnalyzeQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolanalyzesize" title="ThreadPoolAnalyzeSize">ThreadPoolAnalyzeSize</a>" : <i>String</i>,
    "<a href="#threadpoolforcemergesize" title="ThreadPoolForceMergeSize">ThreadPoolForceMergeSize</a>" : <i>String</i>,
    "<a href="#threadpoolgetqueuesize" title="ThreadPoolGetQueueSize">ThreadPoolGetQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolgetsize" title="ThreadPoolGetSize">ThreadPoolGetSize</a>" : <i>String</i>,
    "<a href="#threadpoolindexqueuesize" title="ThreadPoolIndexQueueSize">ThreadPoolIndexQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolindexsize" title="ThreadPoolIndexSize">ThreadPoolIndexSize</a>" : <i>String</i>,
    "<a href="#threadpoolsearchqueuesize" title="ThreadPoolSearchQueueSize">ThreadPoolSearchQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolsearchsize" title="ThreadPoolSearchSize">ThreadPoolSearchSize</a>" : <i>String</i>,
    "<a href="#threadpoolsearchthrottledqueuesize" title="ThreadPoolSearchThrottledQueueSize">ThreadPoolSearchThrottledQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolsearchthrottledsize" title="ThreadPoolSearchThrottledSize">ThreadPoolSearchThrottledSize</a>" : <i>String</i>,
    "<a href="#threadpoolwritequeuesize" title="ThreadPoolWriteQueueSize">ThreadPoolWriteQueueSize</a>" : <i>String</i>,
    "<a href="#threadpoolwritesize" title="ThreadPoolWriteSize">ThreadPoolWriteSize</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#actionautocreateindexenabled" title="ActionAutoCreateIndexEnabled">ActionAutoCreateIndexEnabled</a>: <i>String</i>
<a href="#actiondestructiverequiresname" title="ActionDestructiveRequiresName">ActionDestructiveRequiresName</a>: <i>String</i>
<a href="#clustermaxshardspernode" title="ClusterMaxShardsPerNode">ClusterMaxShardsPerNode</a>: <i>String</i>
<a href="#httpmaxcontentlength" title="HttpMaxContentLength">HttpMaxContentLength</a>: <i>String</i>
<a href="#httpmaxheadersize" title="HttpMaxHeaderSize">HttpMaxHeaderSize</a>: <i>String</i>
<a href="#httpmaxinitiallinelength" title="HttpMaxInitialLineLength">HttpMaxInitialLineLength</a>: <i>String</i>
<a href="#indicesfielddatacachesize" title="IndicesFielddataCacheSize">IndicesFielddataCacheSize</a>: <i>String</i>
<a href="#indicesmemoryindexbuffersize" title="IndicesMemoryIndexBufferSize">IndicesMemoryIndexBufferSize</a>: <i>String</i>
<a href="#indicesqueriescachesize" title="IndicesQueriesCacheSize">IndicesQueriesCacheSize</a>: <i>String</i>
<a href="#indicesqueryboolmaxclausecount" title="IndicesQueryBoolMaxClauseCount">IndicesQueryBoolMaxClauseCount</a>: <i>String</i>
<a href="#reindexremotewhitelist" title="ReindexRemoteWhitelist">ReindexRemoteWhitelist</a>: <i>
      - String</i>
<a href="#searchmaxbuckets" title="SearchMaxBuckets">SearchMaxBuckets</a>: <i>String</i>
<a href="#threadpoolanalyzequeuesize" title="ThreadPoolAnalyzeQueueSize">ThreadPoolAnalyzeQueueSize</a>: <i>String</i>
<a href="#threadpoolanalyzesize" title="ThreadPoolAnalyzeSize">ThreadPoolAnalyzeSize</a>: <i>String</i>
<a href="#threadpoolforcemergesize" title="ThreadPoolForceMergeSize">ThreadPoolForceMergeSize</a>: <i>String</i>
<a href="#threadpoolgetqueuesize" title="ThreadPoolGetQueueSize">ThreadPoolGetQueueSize</a>: <i>String</i>
<a href="#threadpoolgetsize" title="ThreadPoolGetSize">ThreadPoolGetSize</a>: <i>String</i>
<a href="#threadpoolindexqueuesize" title="ThreadPoolIndexQueueSize">ThreadPoolIndexQueueSize</a>: <i>String</i>
<a href="#threadpoolindexsize" title="ThreadPoolIndexSize">ThreadPoolIndexSize</a>: <i>String</i>
<a href="#threadpoolsearchqueuesize" title="ThreadPoolSearchQueueSize">ThreadPoolSearchQueueSize</a>: <i>String</i>
<a href="#threadpoolsearchsize" title="ThreadPoolSearchSize">ThreadPoolSearchSize</a>: <i>String</i>
<a href="#threadpoolsearchthrottledqueuesize" title="ThreadPoolSearchThrottledQueueSize">ThreadPoolSearchThrottledQueueSize</a>: <i>String</i>
<a href="#threadpoolsearchthrottledsize" title="ThreadPoolSearchThrottledSize">ThreadPoolSearchThrottledSize</a>: <i>String</i>
<a href="#threadpoolwritequeuesize" title="ThreadPoolWriteQueueSize">ThreadPoolWriteQueueSize</a>: <i>String</i>
<a href="#threadpoolwritesize" title="ThreadPoolWriteSize">ThreadPoolWriteSize</a>: <i>String</i>
</pre>

## Properties

#### ActionAutoCreateIndexEnabled

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionDestructiveRequiresName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMaxShardsPerNode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMaxContentLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMaxHeaderSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMaxInitialLineLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndicesFielddataCacheSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndicesMemoryIndexBufferSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndicesQueriesCacheSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndicesQueryBoolMaxClauseCount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReindexRemoteWhitelist

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchMaxBuckets

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolAnalyzeQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolAnalyzeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolForceMergeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolGetQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolGetSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolIndexQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolIndexSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolSearchQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolSearchSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolSearchThrottledQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolSearchThrottledSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolWriteQueueSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreadPoolWriteSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

