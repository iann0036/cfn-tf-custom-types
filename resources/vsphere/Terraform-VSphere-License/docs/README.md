# Terraform::VSphere::License

Provides a VMware vSphere license resource. This can be used to add and remove license keys.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::License",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#licensekey" title="LicenseKey">LicenseKey</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::License
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#licensekey" title="LicenseKey">LicenseKey</a>: <i>String</i>
</pre>

## Properties

#### Labels

A map of key/value pairs to be attached as labels (tags) to the license key.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseKey

The license key to add.

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

#### EditionKey

Returns the <code>EditionKey</code> value.

#### Name

Returns the <code>Name</code> value.

#### Total

Returns the <code>Total</code> value.

#### Used

Returns the <code>Used</code> value.

