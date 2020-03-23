# Terraform::AWS::DefaultRouteTable

Provides a resource to manage a Default VPC Routing Table.

Each VPC created in AWS comes with a Default Route Table that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource. It is recommended you **do not** use both `aws_default_route_table` to
manage the default route table **and** use the `aws_main_route_table_association`,
due to possible conflict in routes.

The `aws_default_route_table` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Route
Table that cannot be destroyed, and is created with a single route.

When Terraform first adopts the Default Route Table, it **immediately removes all
defined routes**. It then proceeds to create any routes specified in the
configuration. This step is required so that only the routes specified in the
configuration present in the Default Route Table.

For more information about Route Tables, see the AWS Documentation on
[Route Tables][aws-route-tables].

For more information about managing normal Route Tables in Terraform, see our
documentation on [aws_route_table][tf-route-tables].

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone [Route resource](route.html) and a Route Table resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite routes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DefaultRouteTable",
    "Properties" : {
        "<a href="#defaultroutetableid" title="DefaultRouteTableId">DefaultRouteTableId</a>" : <i>String</i>,
        "<a href="#propagatingvgws" title="PropagatingVgws">PropagatingVgws</a>" : <i>[ String, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="route.md">Route</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DefaultRouteTable
Properties:
    <a href="#defaultroutetableid" title="DefaultRouteTableId">DefaultRouteTableId</a>: <i>String</i>
    <a href="#propagatingvgws" title="PropagatingVgws">PropagatingVgws</a>: <i>
      - String</i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="route.md">Route</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### DefaultRouteTableId

The ID of the Default Routing Table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagatingVgws

A list of virtual gateways for propagation.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

A list of route objects. Their keys are documented below.
This argument is processed in [attribute-as-blocks mode](/docs/configuration/attr-as-blocks.html).

_Required_: No

_Type_: List of <a href="route.md">Route</a>

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

#### Id

Returns the <code>Id</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

