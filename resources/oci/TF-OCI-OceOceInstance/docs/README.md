# TF::OCI::OceOceInstance

This resource provides the Oce Instance resource in Oracle Cloud Infrastructure Content and Experience service.

Creates a new OceInstance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OceOceInstance",
    "Properties" : {
        "<a href="#adminemail" title="AdminEmail">AdminEmail</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>" : <i>String</i>,
        "<a href="#instanceaccesstype" title="InstanceAccessType">InstanceAccessType</a>" : <i>String</i>,
        "<a href="#instancelicensetype" title="InstanceLicenseType">InstanceLicenseType</a>" : <i>String</i>,
        "<a href="#instanceusagetype" title="InstanceUsageType">InstanceUsageType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objectstoragenamespace" title="ObjectStorageNamespace">ObjectStorageNamespace</a>" : <i>String</i>,
        "<a href="#tenancyid" title="TenancyId">TenancyId</a>" : <i>String</i>,
        "<a href="#tenancyname" title="TenancyName">TenancyName</a>" : <i>String</i>,
        "<a href="#upgradeschedule" title="UpgradeSchedule">UpgradeSchedule</a>" : <i>String</i>,
        "<a href="#wafprimarydomain" title="WafPrimaryDomain">WafPrimaryDomain</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OceOceInstance
Properties:
    <a href="#adminemail" title="AdminEmail">AdminEmail</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#idcsaccesstoken" title="IdcsAccessToken">IdcsAccessToken</a>: <i>String</i>
    <a href="#instanceaccesstype" title="InstanceAccessType">InstanceAccessType</a>: <i>String</i>
    <a href="#instancelicensetype" title="InstanceLicenseType">InstanceLicenseType</a>: <i>String</i>
    <a href="#instanceusagetype" title="InstanceUsageType">InstanceUsageType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objectstoragenamespace" title="ObjectStorageNamespace">ObjectStorageNamespace</a>: <i>String</i>
    <a href="#tenancyid" title="TenancyId">TenancyId</a>: <i>String</i>
    <a href="#tenancyname" title="TenancyName">TenancyName</a>: <i>String</i>
    <a href="#upgradeschedule" title="UpgradeSchedule">UpgradeSchedule</a>: <i>String</i>
    <a href="#wafprimarydomain" title="WafPrimaryDomain">WafPrimaryDomain</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminEmail

Admin Email for Notification.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) Compartment Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"foo-namespace.bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) OceInstance description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdcsAccessToken

Identity Cloud Service access token identifying a stripe and service administrator user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceAccessType

Flag indicating whether the instance access is private or public.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceLicenseType

(Updatable) Flag indicating whether the instance license is new cloud or bring your own license.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceUsageType

(Updatable) Instance type based on its usage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

OceInstance Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectStorageNamespace

Object Storage Namespace of Tenancy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenancyId

Tenancy Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenancyName

Tenancy Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSchedule

Upgrade schedule type representing service to be upgraded immediately whenever latest version is released or delay upgrade of the service to previous released version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafPrimaryDomain

(Updatable) Web Application Firewall(WAF) primary domain.

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

#### Guid

Returns the <code>Guid</code> value.

#### Id

Returns the <code>Id</code> value.

#### IdcsTenancy

Returns the <code>IdcsTenancy</code> value.

#### Service

Returns the <code>Service</code> value.

#### State

Returns the <code>State</code> value.

#### StateMessage

Returns the <code>StateMessage</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

