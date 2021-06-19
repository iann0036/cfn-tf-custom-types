# TF::AWS::VpcEndpointServiceAllowedPrincipal

Provides a resource to allow a principal to discover a VPC endpoint service.

~> **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
both a standalone [VPC Endpoint Service Allowed Principal](vpc_endpoint_service_allowed_principal.html) resource
and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
and will overwrite the association.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::VpcEndpointServiceAllowedPrincipal",
    "Properties" : {
        "<a href="#principalarn" title="PrincipalArn">PrincipalArn</a>" : <i>String</i>,
        "<a href="#vpcendpointserviceid" title="VpcEndpointServiceId">VpcEndpointServiceId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::VpcEndpointServiceAllowedPrincipal
Properties:
    <a href="#principalarn" title="PrincipalArn">PrincipalArn</a>: <i>String</i>
    <a href="#vpcendpointserviceid" title="VpcEndpointServiceId">VpcEndpointServiceId</a>: <i>String</i>
</pre>

## Properties

#### PrincipalArn

The ARN of the principal to allow permissions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcEndpointServiceId

The ID of the VPC endpoint service to allow permission.

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

