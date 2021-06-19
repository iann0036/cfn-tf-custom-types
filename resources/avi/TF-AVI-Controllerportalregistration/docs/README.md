# TF::AVI::Controllerportalregistration

The ControllerPortalRegistration resource allows the creation and management of Avi ControllerPortalRegistration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Controllerportalregistration",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#asset" title="Asset">Asset</a>" : <i>[ <a href="assetdefinition.md">AssetDefinition</a>, ... ]</i>,
        "<a href="#portalauth" title="PortalAuth">PortalAuth</a>" : <i>[ <a href="portalauthdefinition.md">PortalAuthDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Controllerportalregistration
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#asset" title="Asset">Asset</a>: <i>
      - <a href="assetdefinition.md">AssetDefinition</a></i>
    <a href="#portalauth" title="PortalAuth">PortalAuth</a>: <i>
      - <a href="portalauthdefinition.md">PortalAuthDefinition</a></i>
</pre>

## Properties

#### Name

Field introduced in 18.2.6.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asset

_Required_: No

_Type_: List of <a href="assetdefinition.md">AssetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalAuth

_Required_: No

_Type_: List of <a href="portalauthdefinition.md">PortalAuthDefinition</a>

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

