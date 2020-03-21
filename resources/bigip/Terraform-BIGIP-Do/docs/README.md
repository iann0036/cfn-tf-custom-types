# Terraform::BIGIP::Do

`bigip_do` provides details about bigip do resource

This resource is helpful to configure do declarative JSON on BIG-IP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::Do",
    "Properties" : {
        "<a href="#dojson" title="DoJson">DoJson</a>" : <i>String</i>,
        "<a href="#tenantname" title="TenantName">TenantName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::Do
Properties:
    <a href="#dojson" title="DoJson">DoJson</a>: <i>String</i>
    <a href="#tenantname" title="TenantName">TenantName</a>: <i>String</i>
</pre>

## Properties

#### DoJson

Name of the of the Declarative DO JSON file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantName

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

