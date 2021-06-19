# TF::AzureAD::ApplicationOauth2Permission

Manages an OAuth2 Permission (also known as a Scope) associated with an Application within Azure Active Directory.

~> This resource is deprecated in favour of [azuread_application_oauth2_permission_scope](application_oauth2_permission_scope.html) and will be removed in version 2.0 of the provider.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureAD::ApplicationOauth2Permission",
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
Type: TF::AzureAD::ApplicationOauth2Permission
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

Permission help text that appears in the admin consent and app assignment experiences.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminConsentDisplayName

Display name for the permission that appears in the admin consent and app assignment experiences.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationObjectId

The Object ID of the Application for which this Permission should be created. Changing this field forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

Determines if the Permission is enabled. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionId

Specifies a custom UUID for the Permission. If omitted, a random UUID will be automatically generated. Changing this field forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies whether this scope permission can be consented to by an end user, or whether it is a tenant-wide permission that must be consented to by an Administrator. Possible values are "User" or "Admin".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDescription

Permission help text that appears in the end user consent experience.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConsentDisplayName

Display name for the permission that appears in the end user consent experience.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the scope claim that the resource application should expect in the OAuth 2.0 access token.

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

