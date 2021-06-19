# TF::Spotinst::ElastigroupAws IntegrationNomadDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acltoken" title="AclToken">AclToken</a>" : <i>String</i>,
    "<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>" : <i>Double</i>,
    "<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>" : <i>Boolean</i>,
    "<a href="#masterhost" title="MasterHost">MasterHost</a>" : <i>String</i>,
    "<a href="#masterport" title="MasterPort">MasterPort</a>" : <i>Double</i>,
    "<a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>" : <i>[ <a href="autoscaleconstraintsdefinition.md">AutoscaleConstraintsDefinition</a>, ... ]</i>,
    "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>, ... ]</i>,
    "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#acltoken" title="AclToken">AclToken</a>: <i>String</i>
<a href="#autoscalecooldown" title="AutoscaleCooldown">AutoscaleCooldown</a>: <i>Double</i>
<a href="#autoscaleisenabled" title="AutoscaleIsEnabled">AutoscaleIsEnabled</a>: <i>Boolean</i>
<a href="#masterhost" title="MasterHost">MasterHost</a>: <i>String</i>
<a href="#masterport" title="MasterPort">MasterPort</a>: <i>Double</i>
<a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>: <i>
      - <a href="autoscaleconstraintsdefinition.md">AutoscaleConstraintsDefinition</a></i>
<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a></i>
<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a></i>
</pre>

## Properties

#### AclToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleCooldown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleIsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterHost

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConstraints

_Required_: No

_Type_: List of <a href="autoscaleconstraintsdefinition.md">AutoscaleConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledowndefinition.md">AutoscaleDownDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroomdefinition.md">AutoscaleHeadroomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

