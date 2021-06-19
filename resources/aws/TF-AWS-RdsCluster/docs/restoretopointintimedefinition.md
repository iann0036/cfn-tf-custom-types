# TF::AWS::RdsCluster RestoreToPointInTimeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#restoretotime" title="RestoreToTime">RestoreToTime</a>" : <i>String</i>,
    "<a href="#restoretype" title="RestoreType">RestoreType</a>" : <i>String</i>,
    "<a href="#sourceclusteridentifier" title="SourceClusterIdentifier">SourceClusterIdentifier</a>" : <i>String</i>,
    "<a href="#uselatestrestorabletime" title="UseLatestRestorableTime">UseLatestRestorableTime</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#restoretotime" title="RestoreToTime">RestoreToTime</a>: <i>String</i>
<a href="#restoretype" title="RestoreType">RestoreType</a>: <i>String</i>
<a href="#sourceclusteridentifier" title="SourceClusterIdentifier">SourceClusterIdentifier</a>: <i>String</i>
<a href="#uselatestrestorabletime" title="UseLatestRestorableTime">UseLatestRestorableTime</a>: <i>Boolean</i>
</pre>

## Properties

#### RestoreToTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceClusterIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLatestRestorableTime

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

