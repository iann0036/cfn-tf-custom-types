# TF::AWS::MainRouteTableAssociation

Provides a resource for managing the main routing table of a VPC.

~> **NOTE:** **Do not** use both `aws_default_route_table` to manage a default route table **and** `aws_main_route_table_association` with the same VPC due to possible route conflicts. See [aws_default_route_table][tf-default-route-table] documentation for more details.
For more information, see the Amazon VPC User Guide on [Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html). For information about managing normal route tables in Terraform, see [`aws_route_table`](/docs/providers/aws/r/route_table.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::MainRouteTableAssociation",
    "Properties" : {
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::MainRouteTableAssociation
Properties:
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### RouteTableId

The ID of the Route Table to set as the new
main route table for the target VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The ID of the VPC whose main route table should be set.

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

#### OriginalRouteTableId

Returns the <code>OriginalRouteTableId</code> value.

