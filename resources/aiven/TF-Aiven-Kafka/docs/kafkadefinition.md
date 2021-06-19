# TF::Aiven::Kafka KafkaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autocreatetopicsenable" title="AutoCreateTopicsEnable">AutoCreateTopicsEnable</a>" : <i>String</i>,
    "<a href="#compressiontype" title="CompressionType">CompressionType</a>" : <i>String</i>,
    "<a href="#connectionsmaxidlems" title="ConnectionsMaxIdleMs">ConnectionsMaxIdleMs</a>" : <i>String</i>,
    "<a href="#defaultreplicationfactor" title="DefaultReplicationFactor">DefaultReplicationFactor</a>" : <i>String</i>,
    "<a href="#groupinitialrebalancedelayms" title="GroupInitialRebalanceDelayMs">GroupInitialRebalanceDelayMs</a>" : <i>String</i>,
    "<a href="#groupmaxsessiontimeoutms" title="GroupMaxSessionTimeoutMs">GroupMaxSessionTimeoutMs</a>" : <i>String</i>,
    "<a href="#groupminsessiontimeoutms" title="GroupMinSessionTimeoutMs">GroupMinSessionTimeoutMs</a>" : <i>String</i>,
    "<a href="#logcleanerdeleteretentionms" title="LogCleanerDeleteRetentionMs">LogCleanerDeleteRetentionMs</a>" : <i>String</i>,
    "<a href="#logcleanermaxcompactionlagms" title="LogCleanerMaxCompactionLagMs">LogCleanerMaxCompactionLagMs</a>" : <i>String</i>,
    "<a href="#logcleanermincleanableratio" title="LogCleanerMinCleanableRatio">LogCleanerMinCleanableRatio</a>" : <i>String</i>,
    "<a href="#logcleanermincompactionlagms" title="LogCleanerMinCompactionLagMs">LogCleanerMinCompactionLagMs</a>" : <i>String</i>,
    "<a href="#logcleanuppolicy" title="LogCleanupPolicy">LogCleanupPolicy</a>" : <i>String</i>,
    "<a href="#logflushintervalmessages" title="LogFlushIntervalMessages">LogFlushIntervalMessages</a>" : <i>String</i>,
    "<a href="#logflushintervalms" title="LogFlushIntervalMs">LogFlushIntervalMs</a>" : <i>String</i>,
    "<a href="#logindexintervalbytes" title="LogIndexIntervalBytes">LogIndexIntervalBytes</a>" : <i>String</i>,
    "<a href="#logindexsizemaxbytes" title="LogIndexSizeMaxBytes">LogIndexSizeMaxBytes</a>" : <i>String</i>,
    "<a href="#logmessagedownconversionenable" title="LogMessageDownconversionEnable">LogMessageDownconversionEnable</a>" : <i>String</i>,
    "<a href="#logmessagetimestampdifferencemaxms" title="LogMessageTimestampDifferenceMaxMs">LogMessageTimestampDifferenceMaxMs</a>" : <i>String</i>,
    "<a href="#logmessagetimestamptype" title="LogMessageTimestampType">LogMessageTimestampType</a>" : <i>String</i>,
    "<a href="#logpreallocate" title="LogPreallocate">LogPreallocate</a>" : <i>String</i>,
    "<a href="#logretentionbytes" title="LogRetentionBytes">LogRetentionBytes</a>" : <i>String</i>,
    "<a href="#logretentionhours" title="LogRetentionHours">LogRetentionHours</a>" : <i>String</i>,
    "<a href="#logretentionms" title="LogRetentionMs">LogRetentionMs</a>" : <i>String</i>,
    "<a href="#logrolljitterms" title="LogRollJitterMs">LogRollJitterMs</a>" : <i>String</i>,
    "<a href="#logrollms" title="LogRollMs">LogRollMs</a>" : <i>String</i>,
    "<a href="#logsegmentbytes" title="LogSegmentBytes">LogSegmentBytes</a>" : <i>String</i>,
    "<a href="#logsegmentdeletedelayms" title="LogSegmentDeleteDelayMs">LogSegmentDeleteDelayMs</a>" : <i>String</i>,
    "<a href="#maxconnectionsperip" title="MaxConnectionsPerIp">MaxConnectionsPerIp</a>" : <i>String</i>,
    "<a href="#maxincrementalfetchsessioncacheslots" title="MaxIncrementalFetchSessionCacheSlots">MaxIncrementalFetchSessionCacheSlots</a>" : <i>String</i>,
    "<a href="#messagemaxbytes" title="MessageMaxBytes">MessageMaxBytes</a>" : <i>String</i>,
    "<a href="#mininsyncreplicas" title="MinInsyncReplicas">MinInsyncReplicas</a>" : <i>String</i>,
    "<a href="#numpartitions" title="NumPartitions">NumPartitions</a>" : <i>String</i>,
    "<a href="#offsetsretentionminutes" title="OffsetsRetentionMinutes">OffsetsRetentionMinutes</a>" : <i>String</i>,
    "<a href="#producerpurgatorypurgeintervalrequests" title="ProducerPurgatoryPurgeIntervalRequests">ProducerPurgatoryPurgeIntervalRequests</a>" : <i>String</i>,
    "<a href="#replicafetchmaxbytes" title="ReplicaFetchMaxBytes">ReplicaFetchMaxBytes</a>" : <i>String</i>,
    "<a href="#replicafetchresponsemaxbytes" title="ReplicaFetchResponseMaxBytes">ReplicaFetchResponseMaxBytes</a>" : <i>String</i>,
    "<a href="#socketrequestmaxbytes" title="SocketRequestMaxBytes">SocketRequestMaxBytes</a>" : <i>String</i>,
    "<a href="#transactionremoveexpiredtransactioncleanupintervalms" title="TransactionRemoveExpiredTransactionCleanupIntervalMs">TransactionRemoveExpiredTransactionCleanupIntervalMs</a>" : <i>String</i>,
    "<a href="#transactionstatelogsegmentbytes" title="TransactionStateLogSegmentBytes">TransactionStateLogSegmentBytes</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autocreatetopicsenable" title="AutoCreateTopicsEnable">AutoCreateTopicsEnable</a>: <i>String</i>
<a href="#compressiontype" title="CompressionType">CompressionType</a>: <i>String</i>
<a href="#connectionsmaxidlems" title="ConnectionsMaxIdleMs">ConnectionsMaxIdleMs</a>: <i>String</i>
<a href="#defaultreplicationfactor" title="DefaultReplicationFactor">DefaultReplicationFactor</a>: <i>String</i>
<a href="#groupinitialrebalancedelayms" title="GroupInitialRebalanceDelayMs">GroupInitialRebalanceDelayMs</a>: <i>String</i>
<a href="#groupmaxsessiontimeoutms" title="GroupMaxSessionTimeoutMs">GroupMaxSessionTimeoutMs</a>: <i>String</i>
<a href="#groupminsessiontimeoutms" title="GroupMinSessionTimeoutMs">GroupMinSessionTimeoutMs</a>: <i>String</i>
<a href="#logcleanerdeleteretentionms" title="LogCleanerDeleteRetentionMs">LogCleanerDeleteRetentionMs</a>: <i>String</i>
<a href="#logcleanermaxcompactionlagms" title="LogCleanerMaxCompactionLagMs">LogCleanerMaxCompactionLagMs</a>: <i>String</i>
<a href="#logcleanermincleanableratio" title="LogCleanerMinCleanableRatio">LogCleanerMinCleanableRatio</a>: <i>String</i>
<a href="#logcleanermincompactionlagms" title="LogCleanerMinCompactionLagMs">LogCleanerMinCompactionLagMs</a>: <i>String</i>
<a href="#logcleanuppolicy" title="LogCleanupPolicy">LogCleanupPolicy</a>: <i>String</i>
<a href="#logflushintervalmessages" title="LogFlushIntervalMessages">LogFlushIntervalMessages</a>: <i>String</i>
<a href="#logflushintervalms" title="LogFlushIntervalMs">LogFlushIntervalMs</a>: <i>String</i>
<a href="#logindexintervalbytes" title="LogIndexIntervalBytes">LogIndexIntervalBytes</a>: <i>String</i>
<a href="#logindexsizemaxbytes" title="LogIndexSizeMaxBytes">LogIndexSizeMaxBytes</a>: <i>String</i>
<a href="#logmessagedownconversionenable" title="LogMessageDownconversionEnable">LogMessageDownconversionEnable</a>: <i>String</i>
<a href="#logmessagetimestampdifferencemaxms" title="LogMessageTimestampDifferenceMaxMs">LogMessageTimestampDifferenceMaxMs</a>: <i>String</i>
<a href="#logmessagetimestamptype" title="LogMessageTimestampType">LogMessageTimestampType</a>: <i>String</i>
<a href="#logpreallocate" title="LogPreallocate">LogPreallocate</a>: <i>String</i>
<a href="#logretentionbytes" title="LogRetentionBytes">LogRetentionBytes</a>: <i>String</i>
<a href="#logretentionhours" title="LogRetentionHours">LogRetentionHours</a>: <i>String</i>
<a href="#logretentionms" title="LogRetentionMs">LogRetentionMs</a>: <i>String</i>
<a href="#logrolljitterms" title="LogRollJitterMs">LogRollJitterMs</a>: <i>String</i>
<a href="#logrollms" title="LogRollMs">LogRollMs</a>: <i>String</i>
<a href="#logsegmentbytes" title="LogSegmentBytes">LogSegmentBytes</a>: <i>String</i>
<a href="#logsegmentdeletedelayms" title="LogSegmentDeleteDelayMs">LogSegmentDeleteDelayMs</a>: <i>String</i>
<a href="#maxconnectionsperip" title="MaxConnectionsPerIp">MaxConnectionsPerIp</a>: <i>String</i>
<a href="#maxincrementalfetchsessioncacheslots" title="MaxIncrementalFetchSessionCacheSlots">MaxIncrementalFetchSessionCacheSlots</a>: <i>String</i>
<a href="#messagemaxbytes" title="MessageMaxBytes">MessageMaxBytes</a>: <i>String</i>
<a href="#mininsyncreplicas" title="MinInsyncReplicas">MinInsyncReplicas</a>: <i>String</i>
<a href="#numpartitions" title="NumPartitions">NumPartitions</a>: <i>String</i>
<a href="#offsetsretentionminutes" title="OffsetsRetentionMinutes">OffsetsRetentionMinutes</a>: <i>String</i>
<a href="#producerpurgatorypurgeintervalrequests" title="ProducerPurgatoryPurgeIntervalRequests">ProducerPurgatoryPurgeIntervalRequests</a>: <i>String</i>
<a href="#replicafetchmaxbytes" title="ReplicaFetchMaxBytes">ReplicaFetchMaxBytes</a>: <i>String</i>
<a href="#replicafetchresponsemaxbytes" title="ReplicaFetchResponseMaxBytes">ReplicaFetchResponseMaxBytes</a>: <i>String</i>
<a href="#socketrequestmaxbytes" title="SocketRequestMaxBytes">SocketRequestMaxBytes</a>: <i>String</i>
<a href="#transactionremoveexpiredtransactioncleanupintervalms" title="TransactionRemoveExpiredTransactionCleanupIntervalMs">TransactionRemoveExpiredTransactionCleanupIntervalMs</a>: <i>String</i>
<a href="#transactionstatelogsegmentbytes" title="TransactionStateLogSegmentBytes">TransactionStateLogSegmentBytes</a>: <i>String</i>
</pre>

## Properties

#### AutoCreateTopicsEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionsMaxIdleMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultReplicationFactor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupInitialRebalanceDelayMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMaxSessionTimeoutMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMinSessionTimeoutMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCleanerDeleteRetentionMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCleanerMaxCompactionLagMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCleanerMinCleanableRatio

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCleanerMinCompactionLagMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCleanupPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFlushIntervalMessages

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFlushIntervalMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogIndexIntervalBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogIndexSizeMaxBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMessageDownconversionEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMessageTimestampDifferenceMaxMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogMessageTimestampType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPreallocate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetentionBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetentionHours

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetentionMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRollJitterMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRollMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSegmentBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSegmentDeleteDelayMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnectionsPerIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIncrementalFetchSessionCacheSlots

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageMaxBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInsyncReplicas

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumPartitions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffsetsRetentionMinutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProducerPurgatoryPurgeIntervalRequests

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaFetchMaxBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaFetchResponseMaxBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SocketRequestMaxBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransactionRemoveExpiredTransactionCleanupIntervalMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransactionStateLogSegmentBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

