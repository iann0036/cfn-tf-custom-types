# TF::FortiOS::SystemSaml

Global settings for SAML authentication.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSaml",
    "Properties" : {
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#defaultloginpage" title="DefaultLoginPage">DefaultLoginPage</a>" : <i>String</i>,
        "<a href="#defaultprofile" title="DefaultProfile">DefaultProfile</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
        "<a href="#idpcert" title="IdpCert">IdpCert</a>" : <i>String</i>,
        "<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>" : <i>String</i>,
        "<a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>" : <i>String</i>,
        "<a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>" : <i>String</i>,
        "<a href="#life" title="Life">Life</a>" : <i>Double</i>,
        "<a href="#portalurl" title="PortalUrl">PortalUrl</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#serveraddress" title="ServerAddress">ServerAddress</a>" : <i>String</i>,
        "<a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>" : <i>String</i>,
        "<a href="#singlesignonurl" title="SingleSignOnUrl">SingleSignOnUrl</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tolerance" title="Tolerance">Tolerance</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#serviceproviders" title="ServiceProviders">ServiceProviders</a>" : <i>[ <a href="serviceprovidersdefinition.md">ServiceProvidersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSaml
Properties:
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#defaultloginpage" title="DefaultLoginPage">DefaultLoginPage</a>: <i>String</i>
    <a href="#defaultprofile" title="DefaultProfile">DefaultProfile</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
    <a href="#idpcert" title="IdpCert">IdpCert</a>: <i>String</i>
    <a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>: <i>String</i>
    <a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>: <i>String</i>
    <a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>: <i>String</i>
    <a href="#life" title="Life">Life</a>: <i>Double</i>
    <a href="#portalurl" title="PortalUrl">PortalUrl</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#serveraddress" title="ServerAddress">ServerAddress</a>: <i>String</i>
    <a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>: <i>String</i>
    <a href="#singlesignonurl" title="SingleSignOnUrl">SingleSignOnUrl</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tolerance" title="Tolerance">Tolerance</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#serviceproviders" title="ServiceProviders">ServiceProviders</a>: <i>
      - <a href="serviceprovidersdefinition.md">ServiceProvidersDefinition</a></i>
</pre>

## Properties

#### Cert

Certificate to sign SAML messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLoginPage

Choose default login page. Valid values: `normal`, `sso`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultProfile

Default profile for new SSO admin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityId

SP entity ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpCert

IDP certificate name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpEntityId

IDP entity ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleLogoutUrl

IDP single logout URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleSignOnUrl

IDP single sign-on URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Life

Length of the range of time when the assertion is valid (in minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalUrl

SP portal URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

SAML role. Valid values: `identity-provider`, `service-provider`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddress

Server address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutUrl

SP single logout URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSignOnUrl

SP single sign-on URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable SAML authentication (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tolerance

Tolerance to the range of time when the assertion is valid (in minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceProviders

_Required_: No

_Type_: List of <a href="serviceprovidersdefinition.md">ServiceProvidersDefinition</a>

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

