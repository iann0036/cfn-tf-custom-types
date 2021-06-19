# TF::AWS::ServicecatalogTagOptionResourceAssociation

Manages a Service Catalog Tag Option Resource Association.

-> **Tip:** A "resource" is either a Service Catalog portfolio or product.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ServicecatalogTagOptionResourceAssociation",
    "Properties" : {
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#tagoptionid" title="TagOptionId">TagOptionId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ServicecatalogTagOptionResourceAssociation
Properties:
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#tagoptionid" title="TagOptionId">TagOptionId</a>: <i>String</i>
</pre>

## Properties

#### ResourceId

Resource identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagOptionId

Tag Option identifier.

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

#### ResourceArn

Returns the <code>ResourceArn</code> value.

#### ResourceCreatedTime

Returns the <code>ResourceCreatedTime</code> value.

#### ResourceDescription

Returns the <code>ResourceDescription</code> value.

#### ResourceName

Returns the <code>ResourceName</code> value.

