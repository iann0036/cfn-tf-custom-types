# TF::AVI::Vcenterserver

The VCenterServer resource allows the creation and management of Avi VCenterServer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Vcenterserver",
    "Properties" : {
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vcentercredentialsref" title="VcenterCredentialsRef">VcenterCredentialsRef</a>" : <i>String</i>,
        "<a href="#vcenterurl" title="VcenterUrl">VcenterUrl</a>" : <i>String</i>,
        "<a href="#contentlib" title="ContentLib">ContentLib</a>" : <i>[ <a href="contentlibdefinition.md">ContentLibDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Vcenterserver
Properties:
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vcentercredentialsref" title="VcenterCredentialsRef">VcenterCredentialsRef</a>: <i>String</i>
    <a href="#vcenterurl" title="VcenterUrl">VcenterUrl</a>: <i>String</i>
    <a href="#contentlib" title="ContentLib">ContentLib</a>: <i>
      - <a href="contentlibdefinition.md">ContentLibDefinition</a></i>
</pre>

## Properties

#### CloudRef

Vcenter belongs to cloud. It is a reference to an object of type cloud. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Availabilty zone where vcenter list belongs to. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Vcenter belongs to tenant. It is a reference to an object of type tenant. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterCredentialsRef

Credentials to access vcenter. It is a reference to an object of type cloudconnectoruser. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterUrl

Vcenter hostname or ip address. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLib

_Required_: No

_Type_: List of <a href="contentlibdefinition.md">ContentLibDefinition</a>

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

