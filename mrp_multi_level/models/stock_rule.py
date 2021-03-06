# Copyright 2020 ForgeFlow S.L. (https://www.forgeflow.com)
# - Héctor Villarreal <hector.villarreal@forgeflow.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _prepare_mo_vals(
        self,
        product_id,
        product_qty,
        product_uom,
        location_id,
        name,
        origin,
        values,
        bom,
    ):
        res = super()._prepare_mo_vals(
            product_id,
            product_qty,
            product_uom,
            location_id,
            name,
            origin,
            values,
            bom,
        )
        if "planned_order_id" in values:
            res["planned_order_id"] = values["planned_order_id"]
        return res
