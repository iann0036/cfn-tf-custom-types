# TF::AzureRM::KeyVaultCertificate KeyPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#curve" title="Curve">Curve</a>" : <i>String</i>,
    "<a href="#exportable" title="Exportable">Exportable</a>" : <i>Boolean</i>,
    "<a href="#keysize" title="KeySize">KeySize</a>" : <i>Double</i>,
    "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
    "<a href="#reusekey" title="ReuseKey">ReuseKey</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#curve" title="Curve">Curve</a>: <i>String</i>
<a href="#exportable" title="Exportable">Exportable</a>: <i>Boolean</i>
<a href="#keysize" title="KeySize">KeySize</a>: <i>Double</i>
<a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
<a href="#reusekey" title="ReuseKey">ReuseKey</a>: <i>Boolean</i>
</pre>

## Properties

#### Curve

Specifies the curve to use when creating an `EC` key. Possible values are `P-256`, `P-256K`, `P-384`, and `P-521`. This field will be required in a future release if `key_type` is `EC` or `EC-HSM`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exportable

Is this certificate exportable? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySize

The size of the key used in the certificate. Possible values include `2048`, `3072`, and `4096` for `RSA` keys, or `256`, `384`, and `521` for `EC` keys. This property is required when using RSA keys. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

Specifies the type of key, such as `RSA` or `EC`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReuseKey

Is the key reusable? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

