# TF::TencentCloud::VodProcedureTemplate

Provide a resource to create a VOD procedure template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::VodProcedureTemplate",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#subappid" title="SubAppId">SubAppId</a>" : <i>Double</i>,
        "<a href="#mediaprocesstask" title="MediaProcessTask">MediaProcessTask</a>" : <i>[ <a href="mediaprocesstaskdefinition.md">MediaProcessTaskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::VodProcedureTemplate
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#subappid" title="SubAppId">SubAppId</a>: <i>Double</i>
    <a href="#mediaprocesstask" title="MediaProcessTask">MediaProcessTask</a>: <i>
      - <a href="mediaprocesstaskdefinition.md">MediaProcessTaskDefinition</a></i>
</pre>

## Properties

#### Comment

Template description. Length limit: 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Task flow name (up to 20 characters).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubAppId

Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediaProcessTask

_Required_: No

_Type_: List of <a href="mediaprocesstaskdefinition.md">MediaProcessTaskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

