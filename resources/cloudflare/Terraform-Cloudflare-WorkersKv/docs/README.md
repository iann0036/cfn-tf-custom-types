# Terraform::Cloudflare::WorkersKv

Provides a Workers KV Pair.  *NOTE:*  This resource uses the Cloudflare account APIs.  This requires setting the `CLOUDFLARE_ACCOUNT_ID` environment variable or `account_id` provider argument.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::WorkersKv",
    "Properties" : {
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::WorkersKv
Properties:
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Key

The key name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

The ID of the Workers KV namespace in which you want to create the KV pair.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The string value to be stored in the key.

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

