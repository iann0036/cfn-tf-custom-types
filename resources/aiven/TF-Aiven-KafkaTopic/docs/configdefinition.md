# TF::Aiven::KafkaTopic ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cleanuppolicy" title="CleanupPolicy">CleanupPolicy</a>" : <i>String</i>,
    "<a href="#compressiontype" title="CompressionType">CompressionType</a>" : <i>String</i>,
    "<a href="#deleteretentionms" title="DeleteRetentionMs">DeleteRetentionMs</a>" : <i>String</i>,
    "<a href="#filedeletedelayms" title="FileDeleteDelayMs">FileDeleteDelayMs</a>" : <i>String</i>,
    "<a href="#flushmessages" title="FlushMessages">FlushMessages</a>" : <i>String</i>,
    "<a href="#flushms" title="FlushMs">FlushMs</a>" : <i>String</i>,
    "<a href="#indexintervalbytes" title="IndexIntervalBytes">IndexIntervalBytes</a>" : <i>String</i>,
    "<a href="#maxcompactionlagms" title="MaxCompactionLagMs">MaxCompactionLagMs</a>" : <i>String</i>,
    "<a href="#maxmessagebytes" title="MaxMessageBytes">MaxMessageBytes</a>" : <i>String</i>,
    "<a href="#messagedownconversionenable" title="MessageDownconversionEnable">MessageDownconversionEnable</a>" : <i>String</i>,
    "<a href="#messageformatversion" title="MessageFormatVersion">MessageFormatVersion</a>" : <i>String</i>,
    "<a href="#messagetimestampdifferencemaxms" title="MessageTimestampDifferenceMaxMs">MessageTimestampDifferenceMaxMs</a>" : <i>String</i>,
    "<a href="#messagetimestamptype" title="MessageTimestampType">MessageTimestampType</a>" : <i>String</i>,
    "<a href="#mincleanabledirtyratio" title="MinCleanableDirtyRatio">MinCleanableDirtyRatio</a>" : <i>String</i>,
    "<a href="#mincompactionlagms" title="MinCompactionLagMs">MinCompactionLagMs</a>" : <i>String</i>,
    "<a href="#mininsyncreplicas" title="MinInsyncReplicas">MinInsyncReplicas</a>" : <i>String</i>,
    "<a href="#preallocate" title="Preallocate">Preallocate</a>" : <i>String</i>,
    "<a href="#retentionbytes" title="RetentionBytes">RetentionBytes</a>" : <i>String</i>,
    "<a href="#retentionms" title="RetentionMs">RetentionMs</a>" : <i>String</i>,
    "<a href="#segmentbytes" title="SegmentBytes">SegmentBytes</a>" : <i>String</i>,
    "<a href="#segmentindexbytes" title="SegmentIndexBytes">SegmentIndexBytes</a>" : <i>String</i>,
    "<a href="#segmentjitterms" title="SegmentJitterMs">SegmentJitterMs</a>" : <i>String</i>,
    "<a href="#segmentms" title="SegmentMs">SegmentMs</a>" : <i>String</i>,
    "<a href="#uncleanleaderelectionenable" title="UncleanLeaderElectionEnable">UncleanLeaderElectionEnable</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cleanuppolicy" title="CleanupPolicy">CleanupPolicy</a>: <i>String</i>
<a href="#compressiontype" title="CompressionType">CompressionType</a>: <i>String</i>
<a href="#deleteretentionms" title="DeleteRetentionMs">DeleteRetentionMs</a>: <i>String</i>
<a href="#filedeletedelayms" title="FileDeleteDelayMs">FileDeleteDelayMs</a>: <i>String</i>
<a href="#flushmessages" title="FlushMessages">FlushMessages</a>: <i>String</i>
<a href="#flushms" title="FlushMs">FlushMs</a>: <i>String</i>
<a href="#indexintervalbytes" title="IndexIntervalBytes">IndexIntervalBytes</a>: <i>String</i>
<a href="#maxcompactionlagms" title="MaxCompactionLagMs">MaxCompactionLagMs</a>: <i>String</i>
<a href="#maxmessagebytes" title="MaxMessageBytes">MaxMessageBytes</a>: <i>String</i>
<a href="#messagedownconversionenable" title="MessageDownconversionEnable">MessageDownconversionEnable</a>: <i>String</i>
<a href="#messageformatversion" title="MessageFormatVersion">MessageFormatVersion</a>: <i>String</i>
<a href="#messagetimestampdifferencemaxms" title="MessageTimestampDifferenceMaxMs">MessageTimestampDifferenceMaxMs</a>: <i>String</i>
<a href="#messagetimestamptype" title="MessageTimestampType">MessageTimestampType</a>: <i>String</i>
<a href="#mincleanabledirtyratio" title="MinCleanableDirtyRatio">MinCleanableDirtyRatio</a>: <i>String</i>
<a href="#mincompactionlagms" title="MinCompactionLagMs">MinCompactionLagMs</a>: <i>String</i>
<a href="#mininsyncreplicas" title="MinInsyncReplicas">MinInsyncReplicas</a>: <i>String</i>
<a href="#preallocate" title="Preallocate">Preallocate</a>: <i>String</i>
<a href="#retentionbytes" title="RetentionBytes">RetentionBytes</a>: <i>String</i>
<a href="#retentionms" title="RetentionMs">RetentionMs</a>: <i>String</i>
<a href="#segmentbytes" title="SegmentBytes">SegmentBytes</a>: <i>String</i>
<a href="#segmentindexbytes" title="SegmentIndexBytes">SegmentIndexBytes</a>: <i>String</i>
<a href="#segmentjitterms" title="SegmentJitterMs">SegmentJitterMs</a>: <i>String</i>
<a href="#segmentms" title="SegmentMs">SegmentMs</a>: <i>String</i>
<a href="#uncleanleaderelectionenable" title="UncleanLeaderElectionEnable">UncleanLeaderElectionEnable</a>: <i>String</i>
</pre>

## Properties

#### CleanupPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRetentionMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileDeleteDelayMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlushMessages

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlushMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexIntervalBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCompactionLagMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMessageBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageDownconversionEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageFormatVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageTimestampDifferenceMaxMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageTimestampType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCleanableDirtyRatio

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCompactionLagMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInsyncReplicas

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preallocate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentIndexBytes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentJitterMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncleanLeaderElectionEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

