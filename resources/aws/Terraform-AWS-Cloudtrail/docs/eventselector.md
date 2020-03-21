# Terraform::AWS::Cloudtrail EventSelector

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#includemanagementevents" title="IncludeManagementEvents">IncludeManagementEvents</a>" : <i>Boolean</i>,
    "<a href="#readwritetype" title="ReadWriteType">ReadWriteType</a>" : <i>String</i>,
    "<a href="#dataresource" title="DataResource">DataResource</a>" : <i>[ <a href="eventselector-dataresource.md">DataResource</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#includemanagementevents" title="IncludeManagementEvents">IncludeManagementEvents</a>: <i>Boolean</i>
<a href="#readwritetype" title="ReadWriteType">ReadWriteType</a>: <i>String</i>
<a href="#dataresource" title="DataResource">DataResource</a>: <i>
      - <a href="eventselector-dataresource.md">DataResource</a></i>
</pre>

## Properties

#### IncludeManagementEvents

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadWriteType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataResource

_Required_: No
_Type_: List of <a href="eventselector-dataresource.md">DataResource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

