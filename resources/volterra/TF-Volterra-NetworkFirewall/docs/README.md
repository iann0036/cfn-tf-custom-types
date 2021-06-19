# TF::Volterra::NetworkFirewall

CloudFormation equivalent of volterra_network_firewall

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::NetworkFirewall",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#disablefastacl" title="DisableFastAcl">DisableFastAcl</a>" : <i>Boolean</i>,
        "<a href="#disableforwardproxypolicy" title="DisableForwardProxyPolicy">DisableForwardProxyPolicy</a>" : <i>Boolean</i>,
        "<a href="#disablenetworkpolicy" title="DisableNetworkPolicy">DisableNetworkPolicy</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#activefastacls" title="ActiveFastAcls">ActiveFastAcls</a>" : <i>[ <a href="activefastaclsdefinition.md">ActiveFastAclsDefinition</a>, ... ]</i>,
        "<a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>" : <i>[ <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>, ... ]</i>,
        "<a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>" : <i>[ <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>, ... ]</i>,
        "<a href="#fastaclset" title="FastAclSet">FastAclSet</a>" : <i>[ <a href="fastaclsetdefinition.md">FastAclSetDefinition</a>, ... ]</i>,
        "<a href="#forwardproxypolicyset" title="ForwardProxyPolicySet">ForwardProxyPolicySet</a>" : <i>[ <a href="forwardproxypolicysetdefinition.md">ForwardProxyPolicySetDefinition</a>, ... ]</i>,
        "<a href="#networkpolicyset" title="NetworkPolicySet">NetworkPolicySet</a>" : <i>[ <a href="networkpolicysetdefinition.md">NetworkPolicySetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::NetworkFirewall
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#disablefastacl" title="DisableFastAcl">DisableFastAcl</a>: <i>Boolean</i>
    <a href="#disableforwardproxypolicy" title="DisableForwardProxyPolicy">DisableForwardProxyPolicy</a>: <i>Boolean</i>
    <a href="#disablenetworkpolicy" title="DisableNetworkPolicy">DisableNetworkPolicy</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#activefastacls" title="ActiveFastAcls">ActiveFastAcls</a>: <i>
      - <a href="activefastaclsdefinition.md">ActiveFastAclsDefinition</a></i>
    <a href="#activeforwardproxypolicies" title="ActiveForwardProxyPolicies">ActiveForwardProxyPolicies</a>: <i>
      - <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a></i>
    <a href="#activenetworkpolicies" title="ActiveNetworkPolicies">ActiveNetworkPolicies</a>: <i>
      - <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a></i>
    <a href="#fastaclset" title="FastAclSet">FastAclSet</a>: <i>
      - <a href="fastaclsetdefinition.md">FastAclSetDefinition</a></i>
    <a href="#forwardproxypolicyset" title="ForwardProxyPolicySet">ForwardProxyPolicySet</a>: <i>
      - <a href="forwardproxypolicysetdefinition.md">ForwardProxyPolicySetDefinition</a></i>
    <a href="#networkpolicyset" title="NetworkPolicySet">NetworkPolicySet</a>: <i>
      - <a href="networkpolicysetdefinition.md">NetworkPolicySetDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableFastAcl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableForwardProxyPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableNetworkPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveFastAcls

_Required_: No

_Type_: List of <a href="activefastaclsdefinition.md">ActiveFastAclsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveForwardProxyPolicies

_Required_: No

_Type_: List of <a href="activeforwardproxypoliciesdefinition.md">ActiveForwardProxyPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveNetworkPolicies

_Required_: No

_Type_: List of <a href="activenetworkpoliciesdefinition.md">ActiveNetworkPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastAclSet

_Required_: No

_Type_: List of <a href="fastaclsetdefinition.md">FastAclSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyPolicySet

_Required_: No

_Type_: List of <a href="forwardproxypolicysetdefinition.md">ForwardProxyPolicySetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicySet

_Required_: No

_Type_: List of <a href="networkpolicysetdefinition.md">NetworkPolicySetDefinition</a>

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

