# Terraform::AzureRM::KeyVaultCertificate CertificatePolicy KeyProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exportable" title="Exportable">Exportable</a>" : <i>Boolean</i>,
    "<a href="#keysize" title="KeySize">KeySize</a>" : <i>Double</i>,
    "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
    "<a href="#reusekey" title="ReuseKey">ReuseKey</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#exportable" title="Exportable">Exportable</a>: <i>Boolean</i>
<a href="#keysize" title="KeySize">KeySize</a>: <i>Double</i>
<a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
<a href="#reusekey" title="ReuseKey">ReuseKey</a>: <i>Boolean</i>
</pre>

## Properties

#### Exportable

Is this Certificate Exportable? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySize

The size of the Key used in the Certificate. Possible values include `2048` and `4096`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

Specifies the Type of Key, such as `RSA`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReuseKey

Is the key reusable? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

