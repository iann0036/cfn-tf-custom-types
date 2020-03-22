# Terraform::Chef::DataBag

A [data bag](http://docs.chef.io/data_bags.html) is a collection of
configuration objects that are stored as JSON in Chef Server and can be
retrieved and used in Chef recipes.

This resource creates the data bag itself. Inside each data bag is a collection
of items which can be created using the ``chef_data_bag_item`` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Chef::DataBag",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Chef::DataBag
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The unique name to assign to the data bag. This is the
name that other server clients will use to find and retrieve data from the
data bag.

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

#### ApiUri

Returns the <code>ApiUri</code> value.

#### Id

Returns the <code>Id</code> value.

