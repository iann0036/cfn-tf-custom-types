# TF::AzureAD::ApplicationOauth2PermissionScope

Manages an OAuth 2.0 Permission Scope associated with an application.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureAD::ApplicationOauth2PermissionScope",
    "Properties" : {
        "<a href="#adminconsentdescription" title="AdminConsentDescription">AdminConsentDescription</a>" : <i>String</i>,
        "<a href="#adminconsentdisplayname" title="AdminConsentDisplayName">AdminConsentDisplayName</a>" : <i>String</i>,
        "<a href="#applicationobjectid" title="ApplicationObjectId">ApplicationObjectId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#permissionid" title="PermissionId">PermissionId</a>" : <i>String</i>,
        "<a href="#scopeid" title="ScopeId">ScopeId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userconsentdescription" title="UserConsentDescription">UserConsentDescription</a>" : <i>String</i>,
        "<a href="#userconsentdisplayname" title="UserConsentDisplayName">UserConsentDisplayName</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureAD::ApplicationOauth2PermissionScope
Properties:
    <a href="#adminconsentdescription" title="AdminConsentDescription">AdminConsentDescription</a>: <i>String</i>
    <a href="#adminconsentdisplayname" title="AdminConsentDisplayName">AdminConsentDisplayName</a>: <i>String</i>
    <a href="#applicationobjectid" title="ApplicationObjectId">ApplicationObjectId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#permissionid" title="PermissionId">PermissionId</a>: <i>String</i>
    <a href="#scopeid" title="ScopeId">ScopeId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userconsentdescription" title="UserConsentDescription">UserConsentDescription</a>: <i>String</i>
    <a href="#userconsentdisplayname" title="UserConsentDisplayName">UserConsentDisplayName</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AdminConsentDescription

Delegated permission description that appears in all tenant-wide admin consent experiences, intended to be read by an administrator granting the permission on behalf of all users.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminConsentDisplayName

Display name for the delegated permission, intended to be read by an administrator granting the permission on behalf of all users.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationObjectId

The Object ID of the Application for which this Permission should be created. Changing this field forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Determines if the permission scope is enabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeId

Specifies a custom UUID for the permission scope. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator should be required for consent to the permissions. Defaults to `User`. Possible values are `User` or `Admin`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDescription

Delegated permission description that appears in the end user consent experience, intended to be read by a user consenting on their own behalf.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDisplayName

Display name for the delegated permission that appears in the end user consent experience.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value that is used for the `scp` claim in OAuth 2.0 access tokens.

_Required_: Yes

_Type_: String

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

