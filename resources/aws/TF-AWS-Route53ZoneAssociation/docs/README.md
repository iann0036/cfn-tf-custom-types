# TF::AWS::Route53ZoneAssociation

Manages a Route53 Hosted Zone VPC association. VPC associations can only be made on private zones. See the [`aws_route53_vpc_association_authorization` resource](route53_vpc_association_authorization.html) for setting up cross-account associations.

~> **NOTE:** Unless explicit association ordering is required (e.g. a separate cross-account association authorization), usage of this resource is not recommended. Use the `vpc` configuration blocks available within the [`aws_route53_zone` resource](/docs/providers/aws/r/route53_zone.html) instead.

~> **NOTE:** Terraform provides both this standalone Zone VPC Association resource and exclusive VPC associations defined in-line in the [`aws_route53_zone` resource](/docs/providers/aws/r/route53_zone.html) via `vpc` configuration blocks. At this time, you cannot use those in-line VPC associations in conjunction with this resource and the same zone ID otherwise it will cause a perpetual difference in plan output. You can optionally use the generic Terraform resour...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53ZoneAssociation",
    "Properties" : {
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcregion" title="VpcRegion">VpcRegion</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53ZoneAssociation
Properties:
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcregion" title="VpcRegion">VpcRegion</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### VpcId

The VPC to associate with the private hosted zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcRegion

The VPC's region. Defaults to the region of the AWS provider.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The private hosted zone to associate.

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

#### OwningAccount

Returns the <code>OwningAccount</code> value.

