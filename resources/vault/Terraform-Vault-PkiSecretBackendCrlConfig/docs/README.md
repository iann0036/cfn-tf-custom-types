# Terraform::Vault::PkiSecretBackendCrlConfig

Allows setting the duration for which the generated CRL should be marked valid. If the CRL is disabled, it will return a signed but zero-length CRL for any request. If enabled, it will re-build the CRL.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::PkiSecretBackendCrlConfig",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#expiry" title="Expiry">Expiry</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::PkiSecretBackendCrlConfig
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#expiry" title="Expiry">Expiry</a>: <i>String</i>
</pre>

## Properties

#### Backend

The path the PKI secret backend is mounted at, with no leading or trailing `/`s.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

Disables or enables CRL building.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiry

Specifies the time until expiration.

_Required_: No

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

