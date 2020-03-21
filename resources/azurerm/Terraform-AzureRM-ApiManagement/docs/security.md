# Terraform::AzureRM::ApiManagement Security

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablebackendssl30" title="EnableBackendSsl30">EnableBackendSsl30</a>" : <i>Boolean</i>,
    "<a href="#enablebackendtls10" title="EnableBackendTls10">EnableBackendTls10</a>" : <i>Boolean</i>,
    "<a href="#enablebackendtls11" title="EnableBackendTls11">EnableBackendTls11</a>" : <i>Boolean</i>,
    "<a href="#enablefrontendssl30" title="EnableFrontendSsl30">EnableFrontendSsl30</a>" : <i>Boolean</i>,
    "<a href="#enablefrontendtls10" title="EnableFrontendTls10">EnableFrontendTls10</a>" : <i>Boolean</i>,
    "<a href="#enablefrontendtls11" title="EnableFrontendTls11">EnableFrontendTls11</a>" : <i>Boolean</i>,
    "<a href="#enabletripledesciphers" title="EnableTripleDesCiphers">EnableTripleDesCiphers</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#enablebackendssl30" title="EnableBackendSsl30">EnableBackendSsl30</a>: <i>Boolean</i>
<a href="#enablebackendtls10" title="EnableBackendTls10">EnableBackendTls10</a>: <i>Boolean</i>
<a href="#enablebackendtls11" title="EnableBackendTls11">EnableBackendTls11</a>: <i>Boolean</i>
<a href="#enablefrontendssl30" title="EnableFrontendSsl30">EnableFrontendSsl30</a>: <i>Boolean</i>
<a href="#enablefrontendtls10" title="EnableFrontendTls10">EnableFrontendTls10</a>: <i>Boolean</i>
<a href="#enablefrontendtls11" title="EnableFrontendTls11">EnableFrontendTls11</a>: <i>Boolean</i>
<a href="#enabletripledesciphers" title="EnableTripleDesCiphers">EnableTripleDesCiphers</a>: <i>Boolean</i>
</pre>

## Properties

#### EnableBackendSsl30

Should SSL 3.0 be enabled on the backend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackendTls10

Should TLS 1.0 be enabled on the backend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackendTls11

Should TLS 1.1 be enabled on the backend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFrontendSsl30

Should SSL 3.0 be enabled on the frontend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFrontendTls10

Should TLS 1.0 be enabled on the frontend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFrontendTls11

Should TLS 1.1 be enabled on the frontend of the gateway? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTripleDesCiphers

Should the `TLS_RSA_WITH_3DES_EDE_CBC_SHA` cipher be enabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

