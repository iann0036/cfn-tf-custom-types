# TF::Alicloud::OosExecution

Provides a OOS Execution resource. For information about Alicloud OOS Execution and how to use it, see [What is Resource Alicloud OOS Execution](https://www.alibabacloud.com/help/doc-detail/120771.htm).

-> **NOTE:** Available in 1.93.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::OosExecution",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#loopmode" title="LoopMode">LoopMode</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>String</i>,
        "<a href="#parentexecutionid" title="ParentExecutionId">ParentExecutionId</a>" : <i>String</i>,
        "<a href="#safetycheck" title="SafetyCheck">SafetyCheck</a>" : <i>String</i>,
        "<a href="#templatecontent" title="TemplateContent">TemplateContent</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#templateversion" title="TemplateVersion">TemplateVersion</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::OosExecution
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#loopmode" title="LoopMode">LoopMode</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>String</i>
    <a href="#parentexecutionid" title="ParentExecutionId">ParentExecutionId</a>: <i>String</i>
    <a href="#safetycheck" title="SafetyCheck">SafetyCheck</a>: <i>String</i>
    <a href="#templatecontent" title="TemplateContent">TemplateContent</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#templateversion" title="TemplateVersion">TemplateVersion</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

The description of OOS Execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopMode

The loop mode of OOS Execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode of OOS Execution. Valid: `Automatic`, `Debug`. Default to `Automatic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

The parameters required by the template. Default to `{}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentExecutionId

The id of parent execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafetyCheck

The mode of safety check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateContent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

The name of execution template.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVersion

The version of execution template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Counters

Returns the <code>Counters</code> value.

#### CreateDate

Returns the <code>CreateDate</code> value.

#### EndDate

Returns the <code>EndDate</code> value.

#### ExecutedBy

Returns the <code>ExecutedBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsParent

Returns the <code>IsParent</code> value.

#### Outputs

Returns the <code>Outputs</code> value.

#### RamRole

Returns the <code>RamRole</code> value.

#### StartDate

Returns the <code>StartDate</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusMessage

Returns the <code>StatusMessage</code> value.

#### TemplateId

Returns the <code>TemplateId</code> value.

#### UpdateDate

Returns the <code>UpdateDate</code> value.

