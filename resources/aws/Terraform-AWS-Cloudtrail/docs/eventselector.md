# Terraform::AWS::Cloudtrail EventSelector

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#includemanagementevents" title="IncludeManagementEvents">IncludeManagementEvents</a>" : <i>Boolean</i>,
    "<a href="#readwritetype" title="ReadWriteType">ReadWriteType</a>" : <i>String</i>,
    "<a href="#dataresource" title="DataResource">DataResource</a>" : <i>[ &lt;a href=&#34;eventselector-dataresource.md&#34;&gt;DataResource&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#includemanagementevents" title="IncludeManagementEvents">IncludeManagementEvents</a>: <i>Boolean</i>
<a href="#readwritetype" title="ReadWriteType">ReadWriteType</a>: <i>String</i>
<a href="#dataresource" title="DataResource">DataResource</a>: <i>
      - &lt;a href=&#34;eventselector-dataresource.md&#34;&gt;DataResource&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;eventselector-dataresource.md&#34;&gt;DataResource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

