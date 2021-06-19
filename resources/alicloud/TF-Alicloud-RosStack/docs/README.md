# TF::Alicloud::RosStack

CloudFormation equivalent of alicloud_ros_stack

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::RosStack",
    "Properties" : {
        "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>String</i>,
        "<a href="#disablerollback" title="DisableRollback">DisableRollback</a>" : <i>Boolean</i>,
        "<a href="#notificationurls" title="NotificationUrls">NotificationUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#ramrolename" title="RamRoleName">RamRoleName</a>" : <i>String</i>,
        "<a href="#replacementoption" title="ReplacementOption">ReplacementOption</a>" : <i>String</i>,
        "<a href="#retainallresources" title="RetainAllResources">RetainAllResources</a>" : <i>Boolean</i>,
        "<a href="#retainresources" title="RetainResources">RetainResources</a>" : <i>[ String, ... ]</i>,
        "<a href="#stackname" title="StackName">StackName</a>" : <i>String</i>,
        "<a href="#stackpolicybody" title="StackPolicyBody">StackPolicyBody</a>" : <i>String</i>,
        "<a href="#stackpolicyduringupdatebody" title="StackPolicyDuringUpdateBody">StackPolicyDuringUpdateBody</a>" : <i>String</i>,
        "<a href="#stackpolicyduringupdateurl" title="StackPolicyDuringUpdateUrl">StackPolicyDuringUpdateUrl</a>" : <i>String</i>,
        "<a href="#stackpolicyurl" title="StackPolicyUrl">StackPolicyUrl</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#templatebody" title="TemplateBody">TemplateBody</a>" : <i>String</i>,
        "<a href="#templateurl" title="TemplateUrl">TemplateUrl</a>" : <i>String</i>,
        "<a href="#templateversion" title="TemplateVersion">TemplateVersion</a>" : <i>String</i>,
        "<a href="#timeoutinminutes" title="TimeoutInMinutes">TimeoutInMinutes</a>" : <i>Double</i>,
        "<a href="#usepreviousparameters" title="UsePreviousParameters">UsePreviousParameters</a>" : <i>Boolean</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::RosStack
Properties:
    <a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>String</i>
    <a href="#disablerollback" title="DisableRollback">DisableRollback</a>: <i>Boolean</i>
    <a href="#notificationurls" title="NotificationUrls">NotificationUrls</a>: <i>
      - String</i>
    <a href="#ramrolename" title="RamRoleName">RamRoleName</a>: <i>String</i>
    <a href="#replacementoption" title="ReplacementOption">ReplacementOption</a>: <i>String</i>
    <a href="#retainallresources" title="RetainAllResources">RetainAllResources</a>: <i>Boolean</i>
    <a href="#retainresources" title="RetainResources">RetainResources</a>: <i>
      - String</i>
    <a href="#stackname" title="StackName">StackName</a>: <i>String</i>
    <a href="#stackpolicybody" title="StackPolicyBody">StackPolicyBody</a>: <i>String</i>
    <a href="#stackpolicyduringupdatebody" title="StackPolicyDuringUpdateBody">StackPolicyDuringUpdateBody</a>: <i>String</i>
    <a href="#stackpolicyduringupdateurl" title="StackPolicyDuringUpdateUrl">StackPolicyDuringUpdateUrl</a>: <i>String</i>
    <a href="#stackpolicyurl" title="StackPolicyUrl">StackPolicyUrl</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#templatebody" title="TemplateBody">TemplateBody</a>: <i>String</i>
    <a href="#templateurl" title="TemplateUrl">TemplateUrl</a>: <i>String</i>
    <a href="#templateversion" title="TemplateVersion">TemplateVersion</a>: <i>String</i>
    <a href="#timeoutinminutes" title="TimeoutInMinutes">TimeoutInMinutes</a>: <i>Double</i>
    <a href="#usepreviousparameters" title="UsePreviousParameters">UsePreviousParameters</a>: <i>Boolean</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CreateOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRollback

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamRoleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacementOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainAllResources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainResources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackPolicyBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackPolicyDuringUpdateBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackPolicyDuringUpdateUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackPolicyUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePreviousParameters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

