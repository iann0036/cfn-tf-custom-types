# Terraform::Vault::KubernetesAuthBackendConfig

Manages an Kubernetes auth backend config in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/kubernetes.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::KubernetesAuthBackendConfig",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#kubernetescacert" title="KubernetesCaCert">KubernetesCaCert</a>" : <i>String</i>,
        "<a href="#kuberneteshost" title="KubernetesHost">KubernetesHost</a>" : <i>String</i>,
        "<a href="#pemkeys" title="PemKeys">PemKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenreviewerjwt" title="TokenReviewerJwt">TokenReviewerJwt</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::KubernetesAuthBackendConfig
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#kubernetescacert" title="KubernetesCaCert">KubernetesCaCert</a>: <i>String</i>
    <a href="#kuberneteshost" title="KubernetesHost">KubernetesHost</a>: <i>String</i>
    <a href="#pemkeys" title="PemKeys">PemKeys</a>: <i>
      - String</i>
    <a href="#tokenreviewerjwt" title="TokenReviewerJwt">TokenReviewerJwt</a>: <i>String</i>
</pre>

## Properties

#### Backend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

Optional JWT issuer. If no issuer is specified, `kubernetes.io/serviceaccount` will be used as the default issuer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesCaCert

PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesHost

Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PemKeys

List of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenReviewerJwt

A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API.

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

