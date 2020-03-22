# Terraform::Netlify::DeployKey

Creates a new netlify deploy key, typically used by the `netlify_site` resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Netlify::DeployKey",
    "Properties" : {
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Netlify::DeployKey
Properties:
</pre>

## Properties

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

#### PublicKey

Returns the <code>PublicKey</code> value.

