# TF::Transloadit::Template

Manages Transloadit Templates. 
For additional details please refer to the [Transloadit documentation](https://transloadit.com/docs/)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Transloadit::Template",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#requiresignatureauth" title="RequireSignatureAuth">RequireSignatureAuth</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Transloadit::Template
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#requiresignatureauth" title="RequireSignatureAuth">RequireSignatureAuth</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### Name

name of the Template to be added
- `template` - (Required) JSON string of the Template's Assembly Instructions. The top-level object must be the JSON object with a `"steps"` key. For more details, see [Assembly Instructions](https://transloadit.com/docs/#assembly-instructions)
- `require_signature_auth` - (Optional - boolean) Use true to deny requests that do not include a signature. With [Signature Authentication](https://transloadit.com/docs/#signature-authentication) you can ensure no one else is sending requests on your behalf. Default value: false.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSignatureAuth

Use true to deny requests that do not include a signature. With [Signature Authentication](https://transloadit.com/docs/#signature-authentication) you can ensure no one else is sending requests on your behalf. Default value: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

JSON string of the Template's Assembly Instructions. The top-level object must be the JSON object with a `"steps"` key. For more details, see [Assembly Instructions](https://transloadit.com/docs/#assembly-instructions)
- `require_signature_auth` - (Optional - boolean) Use true to deny requests that do not include a signature. With [Signature Authentication](https://transloadit.com/docs/#signature-authentication) you can ensure no one else is sending requests on your behalf. Default value: false.

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

