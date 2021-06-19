# TF::AzureAD::Application Oauth2PermissionScopeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminconsentdescription" title="AdminConsentDescription">AdminConsentDescription</a>" : <i>String</i>,
    "<a href="#adminconsentdisplayname" title="AdminConsentDisplayName">AdminConsentDisplayName</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#userconsentdescription" title="UserConsentDescription">UserConsentDescription</a>" : <i>String</i>,
    "<a href="#userconsentdisplayname" title="UserConsentDisplayName">UserConsentDisplayName</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminconsentdescription" title="AdminConsentDescription">AdminConsentDescription</a>: <i>String</i>
<a href="#adminconsentdisplayname" title="AdminConsentDisplayName">AdminConsentDisplayName</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#userconsentdescription" title="UserConsentDescription">UserConsentDescription</a>: <i>String</i>
<a href="#userconsentdisplayname" title="UserConsentDisplayName">UserConsentDisplayName</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AdminConsentDescription

Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminConsentDisplayName

Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Determines if the permission scope is enabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

The unique identifier of the delegated permission. Must be a valid UUID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions. Defaults to `User`. Possible values are `User` or `Admin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDescription

Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDisplayName

Display name for the delegated permission that appears in the end user consent experience.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value that is used for the `scp` claim in OAuth 2.0 access tokens.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

