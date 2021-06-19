# TF::Google::AccessContextManagerServicePerimeter StatusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesslevels" title="AccessLevels">AccessLevels</a>" : <i>[ String, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
    "<a href="#restrictedservices" title="RestrictedServices">RestrictedServices</a>" : <i>[ String, ... ]</i>,
    "<a href="#egresspolicies" title="EgressPolicies">EgressPolicies</a>" : <i>[ <a href="egresspoliciesdefinition.md">EgressPoliciesDefinition</a>, ... ]</i>,
    "<a href="#ingresspolicies" title="IngressPolicies">IngressPolicies</a>" : <i>[ <a href="ingresspoliciesdefinition.md">IngressPoliciesDefinition</a>, ... ]</i>,
    "<a href="#vpcaccessibleservices" title="VpcAccessibleServices">VpcAccessibleServices</a>" : <i>[ <a href="vpcaccessibleservicesdefinition.md">VpcAccessibleServicesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesslevels" title="AccessLevels">AccessLevels</a>: <i>
      - String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
<a href="#restrictedservices" title="RestrictedServices">RestrictedServices</a>: <i>
      - String</i>
<a href="#egresspolicies" title="EgressPolicies">EgressPolicies</a>: <i>
      - <a href="egresspoliciesdefinition.md">EgressPoliciesDefinition</a></i>
<a href="#ingresspolicies" title="IngressPolicies">IngressPolicies</a>: <i>
      - <a href="ingresspoliciesdefinition.md">IngressPoliciesDefinition</a></i>
<a href="#vpcaccessibleservices" title="VpcAccessibleServices">VpcAccessibleServices</a>: <i>
      - <a href="vpcaccessibleservicesdefinition.md">VpcAccessibleServicesDefinition</a></i>
</pre>

## Properties

#### AccessLevels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedServices

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressPolicies

_Required_: No

_Type_: List of <a href="egresspoliciesdefinition.md">EgressPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressPolicies

_Required_: No

_Type_: List of <a href="ingresspoliciesdefinition.md">IngressPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcAccessibleServices

_Required_: No

_Type_: List of <a href="vpcaccessibleservicesdefinition.md">VpcAccessibleServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

