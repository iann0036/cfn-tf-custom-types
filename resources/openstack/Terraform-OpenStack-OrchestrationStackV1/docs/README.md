# Terraform::OpenStack::OrchestrationStackV1

Manages a V1 stack resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::OrchestrationStackV1",
    "Properties" : {
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#creationtime" title="CreationTime">CreationTime</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablerollback" title="DisableRollback">DisableRollback</a>" : <i>Boolean</i>,
        "<a href="#environmentopts" title="EnvironmentOpts">EnvironmentOpts</a>" : <i>[ <a href="environmentopts.md">EnvironmentOpts</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationtopics" title="NotificationTopics">NotificationTopics</a>" : <i>[ String, ... ]</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#statusreason" title="StatusReason">StatusReason</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#templatedescription" title="TemplateDescription">TemplateDescription</a>" : <i>String</i>,
        "<a href="#templateopts" title="TemplateOpts">TemplateOpts</a>" : <i>[ <a href="templateopts.md">TemplateOpts</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#updatedtime" title="UpdatedTime">UpdatedTime</a>" : <i>String</i>,
        "<a href="#outputs" title="Outputs">Outputs</a>" : <i>[ <a href="outputs.md">Outputs</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::OrchestrationStackV1
Properties:
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - String</i>
    <a href="#creationtime" title="CreationTime">CreationTime</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablerollback" title="DisableRollback">DisableRollback</a>: <i>Boolean</i>
    <a href="#environmentopts" title="EnvironmentOpts">EnvironmentOpts</a>: <i>
      - <a href="environmentopts.md">EnvironmentOpts</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationtopics" title="NotificationTopics">NotificationTopics</a>: <i>
      - String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#statusreason" title="StatusReason">StatusReason</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#templatedescription" title="TemplateDescription">TemplateDescription</a>: <i>String</i>
    <a href="#templateopts" title="TemplateOpts">TemplateOpts</a>: <i>
      - <a href="templateopts.md">TemplateOpts</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#updatedtime" title="UpdatedTime">UpdatedTime</a>: <i>String</i>
    <a href="#outputs" title="Outputs">Outputs</a>: <i>
      - <a href="outputs.md">Outputs</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Capabilities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRollback

Enables or disables deletion of all stack
resources when a stack creation fails. Default is true, meaning all
resources are not deleted when stack creation fails.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentOpts

Environment key/value pairs to associate with
the stack which contains details for the environment of the stack.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Environment Opts.

_Required_: No

_Type_: List of <a href="environmentopts.md">EnvironmentOpts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the stack. It must start with an
alphabetic character. Changing this updates the stack's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTopics

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

User-defined key/value pairs as parameters to pass
to the template. Changing this updates the existing stack parameters.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the stack. If
omitted, the `region` argument of the provider is used. Changing this
creates a new stack.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusReason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to assosciate with the Stack.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateOpts

Template key/value pairs to associate with the
stack which contains either the template file or url.
Allowed keys: Bin, URL, Files. Changing this updates the existing stack
Template Opts.

_Required_: Yes

_Type_: List of <a href="templateopts.md">TemplateOpts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The timeout for stack action in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatedTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outputs

_Required_: No

_Type_: List of <a href="outputs.md">Outputs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

