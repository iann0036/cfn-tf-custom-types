# Terraform::AWS::VpcEndpointService

Provides a VPC Endpoint Service resource.
Service consumers can create an _Interface_ [VPC Endpoint](vpc_endpoint.html) to connect to the service.

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
    "Type" : "Terraform::AWS::VpcEndpointService",
    "Properties" : {
        "<a href="#acceptancerequired" title="AcceptanceRequired">AcceptanceRequired</a>" : <i>Boolean</i>,
        "<a href="#allowedprincipals" title="AllowedPrincipals">AllowedPrincipals</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkloadbalancerarns" title="NetworkLoadBalancerArns">NetworkLoadBalancerArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::VpcEndpointService
Properties:
    <a href="#acceptancerequired" title="AcceptanceRequired">AcceptanceRequired</a>: <i>Boolean</i>
    <a href="#allowedprincipals" title="AllowedPrincipals">AllowedPrincipals</a>: <i>
      - String</i>
    <a href="#networkloadbalancerarns" title="NetworkLoadBalancerArns">NetworkLoadBalancerArns</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AcceptanceRequired

Whether or not VPC endpoint connection requests to the service must be accepted by the service owner - `true` or `false`.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedPrincipals

The ARNs of one or more principals allowed to discover the endpoint service.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkLoadBalancerArns

The ARNs of one or more Network Load Balancers for the endpoint service.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailabilityZones

Returns the <code>AvailabilityZones</code> value.

#### BaseEndpointDnsNames

Returns the <code>BaseEndpointDnsNames</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagesVpcEndpoints

Returns the <code>ManagesVpcEndpoints</code> value.

#### PrivateDnsName

Returns the <code>PrivateDnsName</code> value.

#### ServiceName

Returns the <code>ServiceName</code> value.

#### ServiceType

Returns the <code>ServiceType</code> value.

#### State

Returns the <code>State</code> value.

