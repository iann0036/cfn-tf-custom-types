# Terraform::AWS::EmrCluster KerberosAttributes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addomainjoinpassword" title="AdDomainJoinPassword">AdDomainJoinPassword</a>" : <i>String</i>,
    "<a href="#addomainjoinuser" title="AdDomainJoinUser">AdDomainJoinUser</a>" : <i>String</i>,
    "<a href="#crossrealmtrustprincipalpassword" title="CrossRealmTrustPrincipalPassword">CrossRealmTrustPrincipalPassword</a>" : <i>String</i>,
    "<a href="#kdcadminpassword" title="KdcAdminPassword">KdcAdminPassword</a>" : <i>String</i>,
    "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addomainjoinpassword" title="AdDomainJoinPassword">AdDomainJoinPassword</a>: <i>String</i>
<a href="#addomainjoinuser" title="AdDomainJoinUser">AdDomainJoinUser</a>: <i>String</i>
<a href="#crossrealmtrustprincipalpassword" title="CrossRealmTrustPrincipalPassword">CrossRealmTrustPrincipalPassword</a>: <i>String</i>
<a href="#kdcadminpassword" title="KdcAdminPassword">KdcAdminPassword</a>: <i>String</i>
<a href="#realm" title="Realm">Realm</a>: <i>String</i>
</pre>

## Properties

#### AdDomainJoinPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdDomainJoinUser

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossRealmTrustPrincipalPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KdcAdminPassword

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

