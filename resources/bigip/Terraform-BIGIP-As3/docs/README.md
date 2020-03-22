# Terraform::BIGIP::As3

`bigip_as3` provides details about bigip as3 resource

This resource is helpful to configure as3 declarative JSON on BIG-IP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::As3",
    "Properties" : {
        "<a href="#as3json" title="As3Json">As3Json</a>" : <i>String</i>,
        "<a href="#tenantname" title="TenantName">TenantName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::As3
Properties:
    <a href="#as3json" title="As3Json">As3Json</a>: <i>String</i>
    <a href="#tenantname" title="TenantName">TenantName</a>: <i>String</i>
</pre>

## Properties

#### As3Json

Path/Filename of Declarative AS3 JSON which can be a template/json file used with builtin ```templatefile``` function (or) ```file``` function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantName

Tenant name used to set the terraform state changes for as3 resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

