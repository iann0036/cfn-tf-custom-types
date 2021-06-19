# TF::AVI::Systemlimits ControllerLimitsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatespervirtualservice" title="CertificatesPerVirtualservice">CertificatesPerVirtualservice</a>" : <i>Double</i>,
    "<a href="#defaultroutespervrfcontext" title="DefaultRoutesPerVrfcontext">DefaultRoutesPerVrfcontext</a>" : <i>Double</i>,
    "<a href="#ipsperipgroup" title="IpsPerIpgroup">IpsPerIpgroup</a>" : <i>Double</i>,
    "<a href="#poolgroupspervirtualservice" title="PoolgroupsPerVirtualservice">PoolgroupsPerVirtualservice</a>" : <i>Double</i>,
    "<a href="#poolsperpoolgroup" title="PoolsPerPoolgroup">PoolsPerPoolgroup</a>" : <i>Double</i>,
    "<a href="#poolspervirtualservice" title="PoolsPerVirtualservice">PoolsPerVirtualservice</a>" : <i>Double</i>,
    "<a href="#routespervrfcontext" title="RoutesPerVrfcontext">RoutesPerVrfcontext</a>" : <i>Double</i>,
    "<a href="#rulesperhttppolicy" title="RulesPerHttppolicy">RulesPerHttppolicy</a>" : <i>Double</i>,
    "<a href="#rulespernetworksecuritypolicy" title="RulesPerNetworksecuritypolicy">RulesPerNetworksecuritypolicy</a>" : <i>Double</i>,
    "<a href="#serversperpool" title="ServersPerPool">ServersPerPool</a>" : <i>Double</i>,
    "<a href="#snichildrenperparent" title="SniChildrenPerParent">SniChildrenPerParent</a>" : <i>Double</i>,
    "<a href="#stringsperstringgroup" title="StringsPerStringgroup">StringsPerStringgroup</a>" : <i>Double</i>,
    "<a href="#vsbgpscaleout" title="VsBgpScaleout">VsBgpScaleout</a>" : <i>Double</i>,
    "<a href="#vsl2scaleout" title="VsL2Scaleout">VsL2Scaleout</a>" : <i>Double</i>,
    "<a href="#controllercloudlimits" title="ControllerCloudLimits">ControllerCloudLimits</a>" : <i>[ <a href="controllercloudlimitsdefinition.md">ControllerCloudLimitsDefinition</a>, ... ]</i>,
    "<a href="#controllersizinglimits" title="ControllerSizingLimits">ControllerSizingLimits</a>" : <i>[ <a href="controllersizinglimitsdefinition.md">ControllerSizingLimitsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificatespervirtualservice" title="CertificatesPerVirtualservice">CertificatesPerVirtualservice</a>: <i>Double</i>
<a href="#defaultroutespervrfcontext" title="DefaultRoutesPerVrfcontext">DefaultRoutesPerVrfcontext</a>: <i>Double</i>
<a href="#ipsperipgroup" title="IpsPerIpgroup">IpsPerIpgroup</a>: <i>Double</i>
<a href="#poolgroupspervirtualservice" title="PoolgroupsPerVirtualservice">PoolgroupsPerVirtualservice</a>: <i>Double</i>
<a href="#poolsperpoolgroup" title="PoolsPerPoolgroup">PoolsPerPoolgroup</a>: <i>Double</i>
<a href="#poolspervirtualservice" title="PoolsPerVirtualservice">PoolsPerVirtualservice</a>: <i>Double</i>
<a href="#routespervrfcontext" title="RoutesPerVrfcontext">RoutesPerVrfcontext</a>: <i>Double</i>
<a href="#rulesperhttppolicy" title="RulesPerHttppolicy">RulesPerHttppolicy</a>: <i>Double</i>
<a href="#rulespernetworksecuritypolicy" title="RulesPerNetworksecuritypolicy">RulesPerNetworksecuritypolicy</a>: <i>Double</i>
<a href="#serversperpool" title="ServersPerPool">ServersPerPool</a>: <i>Double</i>
<a href="#snichildrenperparent" title="SniChildrenPerParent">SniChildrenPerParent</a>: <i>Double</i>
<a href="#stringsperstringgroup" title="StringsPerStringgroup">StringsPerStringgroup</a>: <i>Double</i>
<a href="#vsbgpscaleout" title="VsBgpScaleout">VsBgpScaleout</a>: <i>Double</i>
<a href="#vsl2scaleout" title="VsL2Scaleout">VsL2Scaleout</a>: <i>Double</i>
<a href="#controllercloudlimits" title="ControllerCloudLimits">ControllerCloudLimits</a>: <i>
      - <a href="controllercloudlimitsdefinition.md">ControllerCloudLimitsDefinition</a></i>
<a href="#controllersizinglimits" title="ControllerSizingLimits">ControllerSizingLimits</a>: <i>
      - <a href="controllersizinglimitsdefinition.md">ControllerSizingLimitsDefinition</a></i>
</pre>

## Properties

#### CertificatesPerVirtualservice

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRoutesPerVrfcontext

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsPerIpgroup

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolgroupsPerVirtualservice

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolsPerPoolgroup

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolsPerVirtualservice

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutesPerVrfcontext

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesPerHttppolicy

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesPerNetworksecuritypolicy

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServersPerPool

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniChildrenPerParent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringsPerStringgroup

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsBgpScaleout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsL2Scaleout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerCloudLimits

_Required_: No

_Type_: List of <a href="controllercloudlimitsdefinition.md">ControllerCloudLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerSizingLimits

_Required_: No

_Type_: List of <a href="controllersizinglimitsdefinition.md">ControllerSizingLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

