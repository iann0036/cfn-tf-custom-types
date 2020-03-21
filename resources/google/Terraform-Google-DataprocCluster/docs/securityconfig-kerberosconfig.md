# Terraform::Google::DataprocCluster SecurityConfig KerberosConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#crossrealmtrustadminserver" title="CrossRealmTrustAdminServer">CrossRealmTrustAdminServer</a>" : <i>String</i>,
    "<a href="#crossrealmtrustkdc" title="CrossRealmTrustKdc">CrossRealmTrustKdc</a>" : <i>String</i>,
    "<a href="#crossrealmtrustrealm" title="CrossRealmTrustRealm">CrossRealmTrustRealm</a>" : <i>String</i>,
    "<a href="#crossrealmtrustsharedpassworduri" title="CrossRealmTrustSharedPasswordUri">CrossRealmTrustSharedPasswordUri</a>" : <i>String</i>,
    "<a href="#enablekerberos" title="EnableKerberos">EnableKerberos</a>" : <i>Boolean</i>,
    "<a href="#kdcdbkeyuri" title="KdcDbKeyUri">KdcDbKeyUri</a>" : <i>String</i>,
    "<a href="#keypassworduri" title="KeyPasswordUri">KeyPasswordUri</a>" : <i>String</i>,
    "<a href="#keystorepassworduri" title="KeystorePasswordUri">KeystorePasswordUri</a>" : <i>String</i>,
    "<a href="#keystoreuri" title="KeystoreUri">KeystoreUri</a>" : <i>String</i>,
    "<a href="#kmskeyuri" title="KmsKeyUri">KmsKeyUri</a>" : <i>String</i>,
    "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
    "<a href="#rootprincipalpassworduri" title="RootPrincipalPasswordUri">RootPrincipalPasswordUri</a>" : <i>String</i>,
    "<a href="#tgtlifetimehours" title="TgtLifetimeHours">TgtLifetimeHours</a>" : <i>Double</i>,
    "<a href="#truststorepassworduri" title="TruststorePasswordUri">TruststorePasswordUri</a>" : <i>String</i>,
    "<a href="#truststoreuri" title="TruststoreUri">TruststoreUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#crossrealmtrustadminserver" title="CrossRealmTrustAdminServer">CrossRealmTrustAdminServer</a>: <i>String</i>
<a href="#crossrealmtrustkdc" title="CrossRealmTrustKdc">CrossRealmTrustKdc</a>: <i>String</i>
<a href="#crossrealmtrustrealm" title="CrossRealmTrustRealm">CrossRealmTrustRealm</a>: <i>String</i>
<a href="#crossrealmtrustsharedpassworduri" title="CrossRealmTrustSharedPasswordUri">CrossRealmTrustSharedPasswordUri</a>: <i>String</i>
<a href="#enablekerberos" title="EnableKerberos">EnableKerberos</a>: <i>Boolean</i>
<a href="#kdcdbkeyuri" title="KdcDbKeyUri">KdcDbKeyUri</a>: <i>String</i>
<a href="#keypassworduri" title="KeyPasswordUri">KeyPasswordUri</a>: <i>String</i>
<a href="#keystorepassworduri" title="KeystorePasswordUri">KeystorePasswordUri</a>: <i>String</i>
<a href="#keystoreuri" title="KeystoreUri">KeystoreUri</a>: <i>String</i>
<a href="#kmskeyuri" title="KmsKeyUri">KmsKeyUri</a>: <i>String</i>
<a href="#realm" title="Realm">Realm</a>: <i>String</i>
<a href="#rootprincipalpassworduri" title="RootPrincipalPasswordUri">RootPrincipalPasswordUri</a>: <i>String</i>
<a href="#tgtlifetimehours" title="TgtLifetimeHours">TgtLifetimeHours</a>: <i>Double</i>
<a href="#truststorepassworduri" title="TruststorePasswordUri">TruststorePasswordUri</a>: <i>String</i>
<a href="#truststoreuri" title="TruststoreUri">TruststoreUri</a>: <i>String</i>
</pre>

## Properties

#### CrossRealmTrustAdminServer

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossRealmTrustKdc

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossRealmTrustRealm

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossRealmTrustSharedPasswordUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKerberos

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KdcDbKeyUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPasswordUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeystorePasswordUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeystoreUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyUri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPrincipalPasswordUri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgtLifetimeHours

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TruststorePasswordUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TruststoreUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

