# TF::AzureRM::ApiManagement SecurityDefinition

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
    "<a href="#enabletripledesciphers" title="EnableTripleDesCiphers">EnableTripleDesCiphers</a>" : <i>Boolean</i>,
    "<a href="#tlsecdheecdsawithaes128cbcshaciphersenabled" title="TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled">TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsecdheecdsawithaes256cbcshaciphersenabled" title="TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled">TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsecdhersawithaes128cbcshaciphersenabled" title="TlsEcdheRsaWithAes128CbcShaCiphersEnabled">TlsEcdheRsaWithAes128CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsecdhersawithaes256cbcshaciphersenabled" title="TlsEcdheRsaWithAes256CbcShaCiphersEnabled">TlsEcdheRsaWithAes256CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsrsawithaes128cbcsha256ciphersenabled" title="TlsRsaWithAes128CbcSha256CiphersEnabled">TlsRsaWithAes128CbcSha256CiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsrsawithaes128cbcshaciphersenabled" title="TlsRsaWithAes128CbcShaCiphersEnabled">TlsRsaWithAes128CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsrsawithaes128gcmsha256ciphersenabled" title="TlsRsaWithAes128GcmSha256CiphersEnabled">TlsRsaWithAes128GcmSha256CiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsrsawithaes256cbcsha256ciphersenabled" title="TlsRsaWithAes256CbcSha256CiphersEnabled">TlsRsaWithAes256CbcSha256CiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tlsrsawithaes256cbcshaciphersenabled" title="TlsRsaWithAes256CbcShaCiphersEnabled">TlsRsaWithAes256CbcShaCiphersEnabled</a>" : <i>Boolean</i>,
    "<a href="#tripledesciphersenabled" title="TripleDesCiphersEnabled">TripleDesCiphersEnabled</a>" : <i>Boolean</i>
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
<a href="#tlsecdheecdsawithaes128cbcshaciphersenabled" title="TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled">TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsecdheecdsawithaes256cbcshaciphersenabled" title="TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled">TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsecdhersawithaes128cbcshaciphersenabled" title="TlsEcdheRsaWithAes128CbcShaCiphersEnabled">TlsEcdheRsaWithAes128CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsecdhersawithaes256cbcshaciphersenabled" title="TlsEcdheRsaWithAes256CbcShaCiphersEnabled">TlsEcdheRsaWithAes256CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsrsawithaes128cbcsha256ciphersenabled" title="TlsRsaWithAes128CbcSha256CiphersEnabled">TlsRsaWithAes128CbcSha256CiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsrsawithaes128cbcshaciphersenabled" title="TlsRsaWithAes128CbcShaCiphersEnabled">TlsRsaWithAes128CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsrsawithaes128gcmsha256ciphersenabled" title="TlsRsaWithAes128GcmSha256CiphersEnabled">TlsRsaWithAes128GcmSha256CiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsrsawithaes256cbcsha256ciphersenabled" title="TlsRsaWithAes256CbcSha256CiphersEnabled">TlsRsaWithAes256CbcSha256CiphersEnabled</a>: <i>Boolean</i>
<a href="#tlsrsawithaes256cbcshaciphersenabled" title="TlsRsaWithAes256CbcShaCiphersEnabled">TlsRsaWithAes256CbcShaCiphersEnabled</a>: <i>Boolean</i>
<a href="#tripledesciphersenabled" title="TripleDesCiphersEnabled">TripleDesCiphersEnabled</a>: <i>Boolean</i>
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

#### TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled

Should the `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled

Should the `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsEcdheRsaWithAes128CbcShaCiphersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsEcdheRsaWithAes256CbcShaCiphersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRsaWithAes128CbcSha256CiphersEnabled

Should the `TLS_RSA_WITH_AES_128_CBC_SHA256` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRsaWithAes128CbcShaCiphersEnabled

Should the `TLS_RSA_WITH_AES_128_CBC_SHA` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRsaWithAes128GcmSha256CiphersEnabled

Should the `TLS_RSA_WITH_AES_128_GCM_SHA256` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRsaWithAes256CbcSha256CiphersEnabled

Should the `TLS_RSA_WITH_AES_256_CBC_SHA256` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsRsaWithAes256CbcShaCiphersEnabled

Should the `TLS_RSA_WITH_AES_256_CBC_SHA` cipher be enabled? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TripleDesCiphersEnabled

Should the `TLS_RSA_WITH_3DES_EDE_CBC_SHA` cipher be enabled for alL TLS versions (1.0, 1.1 and 1.2)? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

