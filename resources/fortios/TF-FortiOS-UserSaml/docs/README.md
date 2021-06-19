# TF::FortiOS::UserSaml

SAML server entry configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserSaml",
    "Properties" : {
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#idpcert" title="IdpCert">IdpCert</a>" : <i>String</i>,
        "<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>" : <i>String</i>,
        "<a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>" : <i>String</i>,
        "<a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>" : <i>String</i>,
        "<a href="#singlesignonurl" title="SingleSignOnUrl">SingleSignOnUrl</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserSaml
Properties:
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#idpcert" title="IdpCert">IdpCert</a>: <i>String</i>
    <a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>: <i>String</i>
    <a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>: <i>String</i>
    <a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>: <i>String</i>
    <a href="#singlesignonurl" title="SingleSignOnUrl">SingleSignOnUrl</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Cert

Certificate to sign SAML messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityId

SP entity ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

Group name in assertion statement.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpCert

IDP Certificate name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpEntityId

IDP entity ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleLogoutUrl

IDP single logout url.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleSignOnUrl

IDP single sign-on URL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SAML server entry name.

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

User name in assertion statement.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

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

