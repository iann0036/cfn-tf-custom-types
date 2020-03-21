# Terraform::Vault::AwsAuthBackendLogin

CloudFormation equivalent of vault_aws_auth_backend_login

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AwsAuthBackendLogin",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#iamhttprequestmethod" title="IamHttpRequestMethod">IamHttpRequestMethod</a>" : <i>String</i>,
        "<a href="#iamrequestbody" title="IamRequestBody">IamRequestBody</a>" : <i>String</i>,
        "<a href="#iamrequestheaders" title="IamRequestHeaders">IamRequestHeaders</a>" : <i>String</i>,
        "<a href="#iamrequesturl" title="IamRequestUrl">IamRequestUrl</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>String</i>,
        "<a href="#nonce" title="Nonce">Nonce</a>" : <i>String</i>,
        "<a href="#pkcs7" title="Pkcs7">Pkcs7</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AwsAuthBackendLogin
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#iamhttprequestmethod" title="IamHttpRequestMethod">IamHttpRequestMethod</a>: <i>String</i>
    <a href="#iamrequestbody" title="IamRequestBody">IamRequestBody</a>: <i>String</i>
    <a href="#iamrequestheaders" title="IamRequestHeaders">IamRequestHeaders</a>: <i>String</i>
    <a href="#iamrequesturl" title="IamRequestUrl">IamRequestUrl</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#identity" title="Identity">Identity</a>: <i>String</i>
    <a href="#nonce" title="Nonce">Nonce</a>: <i>String</i>
    <a href="#pkcs7" title="Pkcs7">Pkcs7</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#signature" title="Signature">Signature</a>: <i>String</i>
</pre>

## Properties

#### Backend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamHttpRequestMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestBody

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestHeaders

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nonce

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pkcs7

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

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

#### Accessor

Returns the <code>Accessor</code> value.

#### AuthType

Returns the <code>AuthType</code> value.

#### ClientToken

Returns the <code>ClientToken</code> value.

#### LeaseDuration

Returns the <code>LeaseDuration</code> value.

#### LeaseStartTime

Returns the <code>LeaseStartTime</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Policies

Returns the <code>Policies</code> value.

#### Renewable

Returns the <code>Renewable</code> value.

