# TF::Google::SqlDatabaseInstance CloneDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#pointintime" title="PointInTime">PointInTime</a>" : <i>String</i>,
    "<a href="#sourceinstancename" title="SourceInstanceName">SourceInstanceName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#pointintime" title="PointInTime">PointInTime</a>: <i>String</i>
<a href="#sourceinstancename" title="SourceInstanceName">SourceInstanceName</a>: <i>String</i>
</pre>

## Properties

#### PointInTime

The timestamp of the point in time that should be restored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInstanceName

Name of the source instance which will be cloned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

