# Terraform::Chef::DataBagItem

A [data bag](http://docs.chef.io/data_bags.html) is a collection of
configuration objects that are stored as JSON in Chef Server and can be
retrieved and used in Chef recipes.

This resource creates objects within an existing data bag. To create the
data bag itself, use the ``chef_data_bag`` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Chef::DataBagItem",
    "Properties" : {
        "<a href="#contentjson" title="ContentJson">ContentJson</a>" : <i>String</i>,
        "<a href="#databagname" title="DataBagName">DataBagName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Chef::DataBagItem
Properties:
    <a href="#contentjson" title="ContentJson">ContentJson</a>: <i>String</i>
    <a href="#databagname" title="DataBagName">DataBagName</a>: <i>String</i>
</pre>

## Properties

#### ContentJson

A string containing a JSON object that will be
the content of the item. Must at minimum contain a property called "id"
that is unique within the data bag, which will become the identifier of
the created item.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataBagName

The name of the data bag into which this item
will be placed.

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

