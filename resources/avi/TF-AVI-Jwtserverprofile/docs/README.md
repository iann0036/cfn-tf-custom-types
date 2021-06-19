# TF::AVI::Jwtserverprofile

The JWTServerProfile resource allows the creation and management of Avi JWTServerProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Jwtserverprofile",
    "Properties" : {
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#jwkskeys" title="JwksKeys">JwksKeys</a>" : <i>String</i>,
        "<a href="#jwtprofiletype" title="JwtProfileType">JwtProfileType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#controllerinternalauth" title="ControllerInternalAuth">ControllerInternalAuth</a>" : <i>[ <a href="controllerinternalauthdefinition.md">ControllerInternalAuthDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Jwtserverprofile
Properties:
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#jwkskeys" title="JwksKeys">JwksKeys</a>: <i>String</i>
    <a href="#jwtprofiletype" title="JwtProfileType">JwtProfileType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#controllerinternalauth" title="ControllerInternalAuth">ControllerInternalAuth</a>: <i>
      - <a href="controllerinternalauthdefinition.md">ControllerInternalAuthDefinition</a></i>
</pre>

## Properties

#### IsFederated

This field describes the object's replication scope. If the field is set to false, then the object is visible within the controller-cluster. If the field is set to true, then the object is replicated across the federation. Field introduced in 20.1.6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

Uniquely identifiable name of the token issuer, only allowed with profile_type client_auth. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwksKeys

Jwks key set used for validating the jwt, only allowed with profile_type client_auth. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtProfileType

Type of jwt server profile which defines the usage type. Enum options - CLIENT_AUTH, CONTROLLER_INTERNAL_AUTH. Field introduced in 20.1.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the jwt profile. Field introduced in 20.1.3.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Uuid of the tenant. It is a reference to an object of type tenant. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerInternalAuth

_Required_: No

_Type_: List of <a href="controllerinternalauthdefinition.md">ControllerInternalAuthDefinition</a>

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

