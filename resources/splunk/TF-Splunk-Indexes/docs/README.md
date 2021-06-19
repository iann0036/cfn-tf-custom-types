# TF::Splunk::Indexes

Create and manage data indexes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::Indexes",
    "Properties" : {
        "<a href="#blocksignsize" title="BlockSignSize">BlockSignSize</a>" : <i>Double</i>,
        "<a href="#bucketrebuildmemoryhint" title="BucketRebuildMemoryHint">BucketRebuildMemoryHint</a>" : <i>String</i>,
        "<a href="#coldpath" title="ColdPath">ColdPath</a>" : <i>String</i>,
        "<a href="#coldtofrozendir" title="ColdToFrozenDir">ColdToFrozenDir</a>" : <i>String</i>,
        "<a href="#coldtofrozenscript" title="ColdToFrozenScript">ColdToFrozenScript</a>" : <i>String</i>,
        "<a href="#compressrawdata" title="CompressRawdata">CompressRawdata</a>" : <i>Boolean</i>,
        "<a href="#datatype" title="Datatype">Datatype</a>" : <i>String</i>,
        "<a href="#enableonlinebucketrepair" title="EnableOnlineBucketRepair">EnableOnlineBucketRepair</a>" : <i>Boolean</i>,
        "<a href="#frozentimeperiodinsecs" title="FrozenTimePeriodInSecs">FrozenTimePeriodInSecs</a>" : <i>Double</i>,
        "<a href="#homepath" title="HomePath">HomePath</a>" : <i>String</i>,
        "<a href="#maxbloombackfillbucketage" title="MaxBloomBackfillBucketAge">MaxBloomBackfillBucketAge</a>" : <i>String</i>,
        "<a href="#maxconcurrentoptimizes" title="MaxConcurrentOptimizes">MaxConcurrentOptimizes</a>" : <i>Double</i>,
        "<a href="#maxdatasize" title="MaxDataSize">MaxDataSize</a>" : <i>String</i>,
        "<a href="#maxhotbuckets" title="MaxHotBuckets">MaxHotBuckets</a>" : <i>Double</i>,
        "<a href="#maxhotidlesecs" title="MaxHotIdleSecs">MaxHotIdleSecs</a>" : <i>Double</i>,
        "<a href="#maxhotspansecs" title="MaxHotSpanSecs">MaxHotSpanSecs</a>" : <i>Double</i>,
        "<a href="#maxmemmb" title="MaxMemMb">MaxMemMb</a>" : <i>Double</i>,
        "<a href="#maxmetaentries" title="MaxMetaEntries">MaxMetaEntries</a>" : <i>Double</i>,
        "<a href="#maxtimeunreplicatednoacks" title="MaxTimeUnreplicatedNoAcks">MaxTimeUnreplicatedNoAcks</a>" : <i>Double</i>,
        "<a href="#maxtimeunreplicatedwithacks" title="MaxTimeUnreplicatedWithAcks">MaxTimeUnreplicatedWithAcks</a>" : <i>Double</i>,
        "<a href="#maxtotaldatasizemb" title="MaxTotalDataSizeMb">MaxTotalDataSizeMb</a>" : <i>Double</i>,
        "<a href="#maxwarmdbcount" title="MaxWarmDbCount">MaxWarmDbCount</a>" : <i>Double</i>,
        "<a href="#minrawfilesyncsecs" title="MinRawFileSyncSecs">MinRawFileSyncSecs</a>" : <i>String</i>,
        "<a href="#minstreamgroupqueuesize" title="MinStreamGroupQueueSize">MinStreamGroupQueueSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partialservicemetaperiod" title="PartialServiceMetaPeriod">PartialServiceMetaPeriod</a>" : <i>Double</i>,
        "<a href="#processtrackerserviceinterval" title="ProcessTrackerServiceInterval">ProcessTrackerServiceInterval</a>" : <i>Double</i>,
        "<a href="#quarantinefuturesecs" title="QuarantineFutureSecs">QuarantineFutureSecs</a>" : <i>Double</i>,
        "<a href="#quarantinepastsecs" title="QuarantinePastSecs">QuarantinePastSecs</a>" : <i>Double</i>,
        "<a href="#rawchunksizebytes" title="RawChunkSizeBytes">RawChunkSizeBytes</a>" : <i>Double</i>,
        "<a href="#repfactor" title="RepFactor">RepFactor</a>" : <i>String</i>,
        "<a href="#rotateperiodinsecs" title="RotatePeriodInSecs">RotatePeriodInSecs</a>" : <i>Double</i>,
        "<a href="#servicemetaperiod" title="ServiceMetaPeriod">ServiceMetaPeriod</a>" : <i>Double</i>,
        "<a href="#syncmeta" title="SyncMeta">SyncMeta</a>" : <i>Boolean</i>,
        "<a href="#thawedpath" title="ThawedPath">ThawedPath</a>" : <i>String</i>,
        "<a href="#throttlecheckperiod" title="ThrottleCheckPeriod">ThrottleCheckPeriod</a>" : <i>Double</i>,
        "<a href="#tstatshomepath" title="TstatsHomePath">TstatsHomePath</a>" : <i>String</i>,
        "<a href="#warmtocoldscript" title="WarmToColdScript">WarmToColdScript</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::Indexes
Properties:
    <a href="#blocksignsize" title="BlockSignSize">BlockSignSize</a>: <i>Double</i>
    <a href="#bucketrebuildmemoryhint" title="BucketRebuildMemoryHint">BucketRebuildMemoryHint</a>: <i>String</i>
    <a href="#coldpath" title="ColdPath">ColdPath</a>: <i>String</i>
    <a href="#coldtofrozendir" title="ColdToFrozenDir">ColdToFrozenDir</a>: <i>String</i>
    <a href="#coldtofrozenscript" title="ColdToFrozenScript">ColdToFrozenScript</a>: <i>String</i>
    <a href="#compressrawdata" title="CompressRawdata">CompressRawdata</a>: <i>Boolean</i>
    <a href="#datatype" title="Datatype">Datatype</a>: <i>String</i>
    <a href="#enableonlinebucketrepair" title="EnableOnlineBucketRepair">EnableOnlineBucketRepair</a>: <i>Boolean</i>
    <a href="#frozentimeperiodinsecs" title="FrozenTimePeriodInSecs">FrozenTimePeriodInSecs</a>: <i>Double</i>
    <a href="#homepath" title="HomePath">HomePath</a>: <i>String</i>
    <a href="#maxbloombackfillbucketage" title="MaxBloomBackfillBucketAge">MaxBloomBackfillBucketAge</a>: <i>String</i>
    <a href="#maxconcurrentoptimizes" title="MaxConcurrentOptimizes">MaxConcurrentOptimizes</a>: <i>Double</i>
    <a href="#maxdatasize" title="MaxDataSize">MaxDataSize</a>: <i>String</i>
    <a href="#maxhotbuckets" title="MaxHotBuckets">MaxHotBuckets</a>: <i>Double</i>
    <a href="#maxhotidlesecs" title="MaxHotIdleSecs">MaxHotIdleSecs</a>: <i>Double</i>
    <a href="#maxhotspansecs" title="MaxHotSpanSecs">MaxHotSpanSecs</a>: <i>Double</i>
    <a href="#maxmemmb" title="MaxMemMb">MaxMemMb</a>: <i>Double</i>
    <a href="#maxmetaentries" title="MaxMetaEntries">MaxMetaEntries</a>: <i>Double</i>
    <a href="#maxtimeunreplicatednoacks" title="MaxTimeUnreplicatedNoAcks">MaxTimeUnreplicatedNoAcks</a>: <i>Double</i>
    <a href="#maxtimeunreplicatedwithacks" title="MaxTimeUnreplicatedWithAcks">MaxTimeUnreplicatedWithAcks</a>: <i>Double</i>
    <a href="#maxtotaldatasizemb" title="MaxTotalDataSizeMb">MaxTotalDataSizeMb</a>: <i>Double</i>
    <a href="#maxwarmdbcount" title="MaxWarmDbCount">MaxWarmDbCount</a>: <i>Double</i>
    <a href="#minrawfilesyncsecs" title="MinRawFileSyncSecs">MinRawFileSyncSecs</a>: <i>String</i>
    <a href="#minstreamgroupqueuesize" title="MinStreamGroupQueueSize">MinStreamGroupQueueSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partialservicemetaperiod" title="PartialServiceMetaPeriod">PartialServiceMetaPeriod</a>: <i>Double</i>
    <a href="#processtrackerserviceinterval" title="ProcessTrackerServiceInterval">ProcessTrackerServiceInterval</a>: <i>Double</i>
    <a href="#quarantinefuturesecs" title="QuarantineFutureSecs">QuarantineFutureSecs</a>: <i>Double</i>
    <a href="#quarantinepastsecs" title="QuarantinePastSecs">QuarantinePastSecs</a>: <i>Double</i>
    <a href="#rawchunksizebytes" title="RawChunkSizeBytes">RawChunkSizeBytes</a>: <i>Double</i>
    <a href="#repfactor" title="RepFactor">RepFactor</a>: <i>String</i>
    <a href="#rotateperiodinsecs" title="RotatePeriodInSecs">RotatePeriodInSecs</a>: <i>Double</i>
    <a href="#servicemetaperiod" title="ServiceMetaPeriod">ServiceMetaPeriod</a>: <i>Double</i>
    <a href="#syncmeta" title="SyncMeta">SyncMeta</a>: <i>Boolean</i>
    <a href="#thawedpath" title="ThawedPath">ThawedPath</a>: <i>String</i>
    <a href="#throttlecheckperiod" title="ThrottleCheckPeriod">ThrottleCheckPeriod</a>: <i>Double</i>
    <a href="#tstatshomepath" title="TstatsHomePath">TstatsHomePath</a>: <i>String</i>
    <a href="#warmtocoldscript" title="WarmToColdScript">WarmToColdScript</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### BlockSignSize

Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. <br>A recommended value is 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketRebuildMemoryHint

Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make.
<be>Caution: This is an advanced parameter. Inappropriate use of this parameter causes splunkd to not start if rebuild is required. Do not set this parameter unless instructed by Splunk Support.
Default value, auto, varies by the amount of physical RAM on the host<br>
less than 2GB RAM = 67108864 (64MB) tsidx
2GB to 8GB RAM = 134217728 (128MB) tsidx
more than 8GB RAM = 268435456 (256MB) tsidx<br>
Values other than "auto" must be 16MB-1GB. Highest legal value (of the numerical part) is 4294967295 You can specify the value using a size suffix: "16777216" or "16MB" are equivalent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColdPath

An absolute path that contains the colddbs for the index. The path must be readable and writable. Cold databases are opened as needed when searching.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColdToFrozenDir

Destination path for the frozen archive. Use as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory.
<br>
Bucket freezing policy is as follows:<br>
New style buckets (4.2 and on): removes all files but the rawdata<br>
To thaw, run splunk rebuild <bucket dir> on the bucket, then move to the thawed directory<br>
Old style buckets (Pre-4.2): gzip all the .data and .tsidx files<br>
To thaw, gunzip the zipped files and move the bucket into the thawed directory<br>
If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColdToFrozenScript

Path to the archiving script.
<br>If your script requires a program to run it (for example, python), specify the program followed by the path. The script must be in $SPLUNK_HOME/bin or one of its subdirectories.
<br>Splunk software ships with an example archiving script in $SPLUNK_HOME/bin called coldToFrozenExample.py. DO NOT use this example script directly. It uses a default path, and if modified in place any changes are overwritten on upgrade.
<br>It is best to copy the example script to a new file in bin and modify it for your system. Most importantly, change the default archive path to an existing directory that fits your needs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressRawdata

This parameter is ignored. The splunkd process always compresses raw data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datatype

Valid values: (event | metric). Specifies the type of index.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableOnlineBucketRepair

Enables asynchronous "online fsck" bucket repair, which runs concurrently with Splunk software.
When enabled, you do not have to wait until buckets are repaired to start the Splunk platform. However, you might observe a slight performance degratation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrozenTimePeriodInSecs

Number of seconds after which indexed data rolls to frozen.
Defaults to 188697600 (6 years).Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomePath

An absolute path that contains the hot and warm buckets for the index.
Required. Splunk software does not start if an index lacks a valid homePath.
<br>Caution: The path must be readable and writable.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBloomBackfillBucketAge

Valid values are: Integer[m|s|h|d].
<br>If a warm or cold bucket is older than the specified age, do not create or rebuild its bloomfilter. Specify 0 to never rebuild bloomfilters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentOptimizes

The number of concurrent optimize processes that can run against a hot bucket.
This number should be increased if instructed by Splunk Support. Typically the default value should suffice.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDataSize

The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk software to autotune this parameter (recommended).
Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto". A "high volume index" would typically be considered one that gets over 10GB of data per day.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHotBuckets

Maximum hot buckets that can exist per index. Defaults to 3.
<br>When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHotIdleSecs

Maximum life, in seconds, of a hot bucket. Defaults to 0. If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. A value of 0 turns off the idle check (equivalent to INFINITE idle time).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHotSpanSecs

Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMemMb

The amount of memory, expressed in MB, to allocate for buffering a single tsidx file into memory before flushing to disk. Defaults to 5. The default is recommended for all environments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMetaEntries

Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTimeUnreplicatedNoAcks

Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored.
If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies.
Highest legal value is 2147483647. To disable this parameter, set to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTimeUnreplicatedWithAcks

Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering).
Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza.
To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTotalDataSizeMb

The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWarmDbCount

The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times is moved to cold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRawFileSyncSecs

Specify an integer (or "disable") for this parameter.
This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices.
During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files.
If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinStreamGroupQueueSize

Minimum size of the queue that stores events in memory before committing them to a tsidx file.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the index to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialServiceMetaPeriod

Related to serviceMetaPeriod. If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync'ed at serviceMetaPeriod.
partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens.
If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect.
By default it is turned off (zero).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessTrackerServiceInterval

Specifies, in seconds, how often the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. Defaults to 15.
If set to 0, the indexer checks child process status every second.
Highest legal value is 4294967295.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineFutureSecs

Events with timestamp of quarantineFutureSecs newer than "now" are dropped into quarantine bucket. Defaults to 2592000 (30 days).
This is a mechanism to prevent main hot buckets from being polluted with fringe events.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantinePastSecs

Events with timestamp of quarantinePastSecs older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RawChunkSizeBytes

Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepFactor

Index replication control. This parameter applies to only clustering slaves.
auto = Use the master index replication configuration value.
0 = Turn off replication for this index.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotatePeriodInSecs

How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceMetaPeriod

Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds).
You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncMeta

When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThawedPath

An absolute path that contains the thawed (resurrected) databases for the index.
Cannot be defined in terms of a volume definition.
Required. Splunk software does not start if an index lacks a valid thawedPath.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThrottleCheckPeriod

Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TstatsHomePath

Location to store datamodel acceleration TSIDX data for this index. Restart splunkd after changing this parameter.
If specified, it must be defined in terms of a volume definition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarmToColdScript

Path to a script to run when moving data from warm to cold.
This attribute is supported for backwards compatibility with Splunk software versions older than 4.0. Contact Splunk support if you need help configuring this setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

